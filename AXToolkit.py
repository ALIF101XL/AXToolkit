#!/usr/bin/env python3
# Author : ALIF101XL
# license : MIT Indonesia
# Focus : Learning - Study
# -*- coding: utf-8 -*-

"""
AXTOOLKIT - Security Tools Installer
Inspired by Katoolin3, but better and more modular.
Author   : ALIF101XL
License  : MIT Indonesia
Focus    : Learning - Study
Version  : 1.0
"""

import sys
import os

# Ensure we can import local modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.app import AXToolkitApp

def main():
try:
app = AXToolkitApp()
app.run()
except KeyboardInterrupt:
print("\n\n[!] Interrupted by user. Exiting...\n")
sys.exit(0)
except PermissionError:
print("\n[!] Permission denied. Please run as root: sudo python3 AXToolkit.py\n")
sys.exit(1)

if __name__ == "__main__":
main()