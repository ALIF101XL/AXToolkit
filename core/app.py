#!/usr/bin/env python3
# Author : ALIF101XL
# license : MIT Indonesia
# Focus : Learning - Study
# -*- coding: utf-8 -*-

"""
core/app.py - Main application controller
"""

import os
import sys
from core.ui import UI
from core.installer import Installer
from core.system import SystemCheck
from categories.registry import CategoryRegistry


class AXToolkitApp:
VERSION = "1.0"
BANNER = r"""
 __  ___  ___   ________  ___  ________  ________  ___       ________
|\  \|\  \|\  \ |\   __  \|\  \|\   __  \|\   __  \|\  \     |\   ____\
\ \  \ \  \/  /|\ \  \|\  \ \  \ \  \|\  \ \  \|\  \ \  \    \ \  \___|_
 \ \  \ \   ___  \ \   __  \ \  \ \  \\\  \ \  \\\  \ \  \    \ \_____  \
  \ \  \ \  \\ \  \ \  \ \  \ \  \ \  \\\  \ \  \\\  \ \  \____\|____|\  \
   \ \__\ \__\\ \__\ \__\ \__\ \__\ \_______\ \_______\ \_______\____\_\  \
    \|__|\|__| \|__|\|__|\|__|\|__|\|_______|\|_______|\|_______|\_________\
                                                                 \|_________|
    [ Security Tools Installer v{version} ]
    [ Inspired by Katoolin3, reborn in Python3    ]
    [ Author : ALIF101XL S.In,]
    """

def __init__(self):
self.ui = UI()
self.installer = Installer()
self.syscheck = SystemCheck()
self.registry = CategoryRegistry()

def run(self):
self.ui.clear()
self.ui.banner(self.BANNER.format(version = self.VERSION))
self._check_requirements()
self._main_menu()

def _check_requirements(self):
ok, msg = self.syscheck.check_all()
if not ok:
self.ui.error(msg)
sys.exit(1)
self.ui.success("System check passed.")
self.ui.pause()

def _main_menu(self):
while True:
self.ui.clear()
self.ui.banner(self.BANNER.format(version = self.VERSION))
self.ui.section("MAIN MENU")
options = [
  ("1", "Add Kali Linux Repositories"),
  ("2", "View / Install Security Tools"),
  ("3", "Install Classic Katoolin Tools"),
  ("4", "Remove Kali Repositories"),
  ("5", "Update All Installed Tools"),
  ("6", "System Information"),
  ("0", "Exit"),
]
self.ui.menu(options)
choice = self.ui.prompt("Select option")

if choice == "1":
self._add_repos()
elif choice == "2":
self._tools_menu()
elif choice == "3":
self._classic_install()
elif choice == "4":
self._remove_repos()
elif choice == "5":
self._update_tools()
elif choice == "6":
self._sysinfo()
elif choice == "0":
self.ui.info("Goodbye! Stay ethical. 🛡️")
sys.exit(0)
else :
self.ui.warn("Invalid choice. Try again.")
self.ui.pause()

def _add_repos(self):
self.ui.clear()
self.ui.section("ADD KALI LINUX REPOSITORIES")
self.ui.warn("This will add Kali Linux repos to your APT sources.")
self.ui.warn("Only do this on Debian/Ubuntu-based systems!")
confirm = self.ui.prompt("Continue? [y/N]").lower()
if confirm == "y":
success = self.installer.add_kali_repos()
if success:
self.ui.success("Kali repos added and GPG key imported!")
else :
self.ui.error("Failed to add repos. Check logs.")
self.ui.pause()

def _remove_repos(self):
self.ui.clear()
self.ui.section("REMOVE KALI LINUX REPOSITORIES")
self.ui.warn("This will remove Kali Linux repos from your system.")
confirm = self.ui.prompt("Continue? [y/N]").lower()
if confirm == "y":
success = self.installer.remove_kali_repos()
if success:
self.ui.success("Kali repos removed successfully!")
else :
self.ui.error("Failed to remove repos.")
self.ui.pause()

def _tools_menu(self):
while True:
self.ui.clear()
self.ui.section("SECURITY TOOLS - CATEGORIES")
categories = self.registry.get_categories()
options = []
for i, cat in enumerate(categories, 1):
options.append((str(i), f" {
  cat['name']}  [{
  cat['count']} tools]"))
options.append(("a", "Install ALL tools from ALL categories"))
options.append(("0", "Back to Main Menu"))
self.ui.menu(options)
choice = self.ui.prompt("Select category")

if choice == "0":
break
elif choice == "a":
self._install_all_tools()
else :
try:
idx = int(choice) - 1
if 0 <= idx < len(categories):
self._category_menu(categories[idx])
else :
self.ui.warn("Invalid choice.")
self.ui.pause()
except ValueError:
self.ui.warn("Invalid input.")
self.ui.pause()

def _category_menu(self, category):
while True:
self.ui.clear()
self.ui.section(f"CATEGORY: {
  category['name'].upper()}")
self.ui.info(category.get("description", ""))
tools = category["tools"]
options = []
for i, tool in enumerate(tools, 1):
status = self.installer.is_installed(tool["pkg"])
mark = self.ui.check_mark(status)
options.append((str(i), f" {
  mark
} {
  tool['name']} - {
  tool['desc']}"))
options.append(("a", "Install ALL tools in this category"))
options.append(("r", "Remove ALL tools in this category"))
options.append(("0", "Back"))
self.ui.menu(options)
choice = self.ui.prompt("Select tool or action")

if choice == "0":
break
elif choice == "a":
pkgs = [t["pkg"] for t in tools]
self.installer.install_packages(pkgs, self.ui)
self.ui.pause()
elif choice == "r":
pkgs = [t["pkg"] for t in tools]
self.installer.remove_packages(pkgs, self.ui)
self.ui.pause()
else :
try:
idx = int(choice) - 1
if 0 <= idx < len(tools):
self._tool_action(tools[idx])
else :
self.ui.warn("Invalid choice.")
self.ui.pause()
except ValueError:
self.ui.warn("Invalid input.")
self.ui.pause()

def _tool_action(self, tool):
self.ui.clear()
self.ui.section(f"TOOL: {
  tool['name']}")
self.ui.info(f"Package  : {
  tool['pkg']}")
self.ui.info(f"Desc     : {
  tool['desc']}")
installed = self.installer.is_installed(tool["pkg"])
status_str = "INSTALLED ✓" if installed else "NOT INSTALLED ✗"
self.ui.info(f"Status   : {
  status_str
}")
print()

if installed:
options = [("1", "Remove this tool"), ("0", "Back")]
else :
options = [("1", "Install this tool"), ("0", "Back")]

self.ui.menu(options)
choice = self.ui.prompt("Select")
if choice == "1":
if installed:
self.installer.remove_packages([tool["pkg"]], self.ui)
else :
self.installer.install_packages([tool["pkg"]], self.ui)
self.ui.pause()

def _classic_install(self):
self.ui.clear()
self.ui.section("INSTALL CLASSIC KATOOLIN TOOLS")
self.ui.info("This installs the most popular tools used in Katoolin classic.")
confirm = self.ui.prompt("Proceed? [y/N]").lower()
if confirm == "y":
from categories.registry import CLASSIC_TOOLS
self.installer.install_packages(CLASSIC_TOOLS, self.ui)
self.ui.pause()

def _update_tools(self):
self.ui.clear()
self.ui.section("UPDATE ALL INSTALLED TOOLS")
confirm = self.ui.prompt("Run apt update && apt upgrade? [y/N]").lower()
if confirm == "y":
self.installer.update_system(self.ui)
self.ui.pause()

def _install_all_tools(self):
self.ui.clear()
self.ui.section("INSTALL ALL TOOLS")
self.ui.warn("This will install ALL tools from ALL categories!")
self.ui.warn("This may take a long time and use significant disk space.")
confirm = self.ui.prompt("Are you sure? [y/N]").lower()
if confirm == "y":
all_pkgs = self.registry.get_all_packages()
self.installer.install_packages(all_pkgs, self.ui)
self.ui.pause()

def _sysinfo(self):
self.ui.clear()
self.ui.section("SYSTEM INFORMATION")
info = self.syscheck.get_sysinfo()
for key, val in info.items():
self.ui.info(f" {
  key:<20
}: {
  val
}")
self.ui.pause()