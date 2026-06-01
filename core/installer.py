#!/usr/bin/env python3
# Author : ALIF101XL
# license : MIT Indonesia
# Focus : Learning - Study
# -*- coding: utf-8 -*-

"""
core/installer.py - Package installation and repository management
"""

import os
import subprocess
import shutil
from pathlib import Path


KALI_REPO_FILE = "/etc/apt/sources.list.d/kali-rolling.list"
KALI_REPO_LINE = "deb http://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware\n"
KALI_GPG_URL   = "https://archive.kali.org/archive-key.asc"
KALI_GPG_PATH  = "/etc/apt/trusted.gpg.d/kali-archive-keyring.gpg"


class Installer:

    def _run(self, cmd, capture=False):
        """Run a shell command. Returns (returncode, stdout)."""
        try:
            result = subprocess.run(
                cmd,
                shell=isinstance(cmd, str),
                capture_output=capture,
                text=True
            )
            return result.returncode, result.stdout
        except Exception as e:
            return 1, str(e)

    def is_installed(self, pkg: str) -> bool:
        """Check if a package is installed via dpkg."""
        code, out = self._run(
            f"dpkg -s {pkg} 2>/dev/null | grep -q 'Status: install ok installed'",
            capture=True
        )
        return code == 0

    def install_packages(self, pkgs: list, ui=None) -> bool:
        """Install one or more packages via apt-get."""
        if not pkgs:
            return True
        pkg_str = " ".join(pkgs)
        if ui:
            ui.progress(f"Installing: {pkg_str}")
        env = os.environ.copy()
        env["DEBIAN_FRONTEND"] = "noninteractive"
        code, _ = self._run(
            f"apt-get install -y {pkg_str}",
        )
        if code == 0:
            if ui:
                ui.success(f"Installed: {pkg_str}")
            return True
        else:
            if ui:
                ui.error(f"Failed to install some packages. Check apt output above.")
            return False

    def remove_packages(self, pkgs: list, ui=None) -> bool:
        """Remove one or more packages via apt-get."""
        if not pkgs:
            return True
        pkg_str = " ".join(pkgs)
        if ui:
            ui.progress(f"Removing: {pkg_str}")
        code, _ = self._run(f"apt-get remove -y {pkg_str}")
        if code == 0:
            if ui:
                ui.success(f"Removed: {pkg_str}")
            return True
        else:
            if ui:
                ui.error("Failed to remove some packages.")
            return False

    def update_system(self, ui=None) -> bool:
        """apt update && apt upgrade"""
        if ui:
            ui.progress("Running apt update...")
        code, _ = self._run("apt-get update")
        if code != 0:
            if ui:
                ui.error("apt update failed.")
            return False
        if ui:
            ui.progress("Running apt upgrade...")
        code, _ = self._run("apt-get upgrade -y")
        if code == 0:
            if ui:
                ui.success("System updated!")
            return True
        else:
            if ui:
                ui.error("apt upgrade failed.")
            return False

    def add_kali_repos(self) -> bool:
        """Add Kali Linux APT repository and import GPG key."""
        try:
            # Write repo file
            with open(KALI_REPO_FILE, "w") as f:
                f.write(KALI_REPO_LINE)

            # Download and import GPG key
            wget = shutil.which("wget") or shutil.which("curl")
            if not wget:
                return False

            if "wget" in wget:
                cmd = f"wget -q -O {KALI_GPG_PATH} {KALI_GPG_URL}"
            else:
                cmd = f"curl -fsSL {KALI_GPG_URL} -o {KALI_GPG_PATH}"

            code, _ = self._run(cmd)
            if code != 0:
                return False

            # apt update
            code, _ = self._run("apt-get update")
            return code == 0

        except PermissionError:
            return False
        except Exception:
            return False

    def remove_kali_repos(self) -> bool:
        """Remove Kali Linux APT repository and GPG key."""
        try:
            for path in [KALI_REPO_FILE, KALI_GPG_PATH]:
                if Path(path).exists():
                    os.remove(path)
            self._run("apt-get update")
            return True
        except Exception:
            return False
