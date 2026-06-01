#!/usr/bin/env python3
# Author : ALIF101XL
# license : MIT Indonesia
# Focus : Learning - Study
# -*- coding: utf-8 -*-

"""
core/ui.py - Terminal UI helpers with colors and formatting
"""

import os
import sys


class Colors:
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
# Foreground
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
# Background
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_BLUE = "\033[44m"


class UI:
WIDTH = 70

def __init__(self):
self.use_color = sys.stdout.isatty()

def _c(self, color, text):
if self.use_color:
return f" {
  color
} {
  text
} {
  Colors.RESET
}"
return text

def clear(self):
os.system("clear" if os.name != "nt" else "cls")

def banner(self, text):
print(self._c(Colors.CYAN + Colors.BOLD, text))

def section(self, title):
line = "─" * self.WIDTH
print(self._c(Colors.CYAN, f"\n {
  '─'*3
} {
  title
} {
  '─'*(self.WIDTH - len(title) - 5)}"))

def menu(self, options):
"""
        options: list of (key, label) tuples
        """
print()
for key, label in options:
key_str = self._c(Colors.YELLOW + Colors.BOLD, f"  [ {
  key
}]")
print(f" {
  key_str
} {
  label
}")
print()

def prompt(self, msg = ""):
arrow = self._c(Colors.GREEN + Colors.BOLD, " ➤ ")
try:
return input(f" {
  arrow
} {
  msg
}: ").strip()
except EOFError:
return ""

def info(self, msg):
print(self._c(Colors.BLUE, f"  [*] ") + msg)

def success(self, msg):
print(self._c(Colors.GREEN, f"  [✓] {
  msg
}"))

def warn(self, msg):
print(self._c(Colors.YELLOW, f"  [!] {
  msg
}"))

def error(self, msg):
print(self._c(Colors.RED, f"  [✗] {
  msg
}"))

def progress(self, msg):
print(self._c(Colors.MAGENTA, f"  [~] {
  msg
}"))

def pause(self, msg = "Press ENTER to continue..."):
print()
input(self._c(Colors.GRAY, f" {
  msg
}"))

def check_mark(self, installed: bool) -> str:
if installed:
return self._c(Colors.GREEN, "✓")
return self._c(Colors.RED, "✗")

def print_separator(self):
print(self._c(Colors.GRAY, "─" * self.WIDTH))

def header(self, text):
pad = (self.WIDTH - len(text) - 4) // 2
line = "═" * self.WIDTH
print(self._c(Colors.CYAN + Colors.BOLD,
f"\n {
  line
}\n {
  '  ' + ' ' * pad + text
}\n {
  line
}"))