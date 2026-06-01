#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
utils/helpers.py - Miscellaneous helper functions
"""

import os
import subprocess
import shutil
from typing import List, Tuple


def run_cmd(cmd: str, capture: bool = False) -> Tuple[int, str]:
    """Run a shell command safely. Returns (returncode, stdout)."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=capture,
            text=True
        )
        return result.returncode, result.stdout or ""
    except Exception as e:
        return 1, str(e)


def is_root() -> bool:
    return os.geteuid() == 0


def command_exists(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def read_file(path: str) -> str:
    """Safely read a text file, return empty string on error."""
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception:
        return ""


def write_file(path: str, content: str) -> bool:
    """Safely write a text file. Returns True on success."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
        return True
    except Exception:
        return False


def format_bytes(size: int) -> str:
    """Convert bytes to human-readable string."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if size < 1024:
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{size:.1f} PB"


def chunk_list(lst: List, n: int) -> List[List]:
    """Split a list into chunks of size n."""
    return [lst[i:i + n] for i in range(0, len(lst), n)]
