#!/usr/bin/env python3
# Author : ALIF101XL
# license : MIT Indonesia
# Focus : Learning - Study
# -*- coding: utf-8 -*-

"""
core/system.py - System requirements and info
"""

import os
import sys
import platform
import shutil
import subprocess


class SystemCheck:

def check_all(self):
"""Run all system checks. Returns (ok, message)."""
checks = [
  self._check_root,
  self._check_os,
  self._check_apt,
]
for check in checks:
ok, msg = check()
if not ok:
return False, msg
return True, "All checks passed."

def _check_root(self):
if os.geteuid() != 0:
return False, "AXToolkit must be run as root. Use: sudo python3 AXToolkit.py"
return True, "Running as root."

def _check_os(self):
system = platform.system()
if system != "Linux":
return False, f"Unsupported OS: {
  system
}. Linux required."
return True, "Linux detected."

def _check_apt(self):
if not shutil.which("apt-get"):
return False, "apt-get not found. Debian/Ubuntu-based system required."
return True, "apt-get found."

def get_sysinfo(self) -> dict:
"""Return a dict of system information."""
info = {}
info["OS"] = platform.system()
info["Distro"] = self._get_distro()
info["Kernel"] = platform.release()
info["Architecture"] = platform.machine()
info["Python"] = platform.python_version()
info["Hostname"] = platform.node()
info["User"] = os.environ.get("USER", "root")
info["APT"] = shutil.which("apt-get") or "Not found"
info["Disk Free"] = self._disk_free()
info["RAM"] = self._ram_info()
return info

def _get_distro(self):
try:
with open("/etc/os-release") as f:
for line in f:
if line.startswith("PRETTY_NAME="):
return line.split("=", 1)[1].strip().strip('"')
except Exception:
pass
return platform.version()

def _disk_free(self):
try:
st = os.statvfs("/")
free_gb = (st.f_bavail * st.f_frsize) / (1024 ** 3)
total_gb = (st.f_blocks * st.f_frsize) / (1024 ** 3)
return f" {
  free_gb:.1f
} GB free / {
  total_gb:.1f
} GB total"
except Exception:
return "Unknown"

def _ram_info(self):
try:
with open("/proc/meminfo") as f:
lines = f.readlines()
mem = {}
for line in lines:
parts = line.split()
if parts[0] in ("MemTotal:", "MemAvailable:"):
mem[parts[0]] = int(parts[1]) // 1024
total = mem.get("MemTotal:", 0)
avail = mem.get("MemAvailable:", 0)
return f" {
  avail
} MB available / {
  total
} MB total"
except Exception:
return "Unknown"