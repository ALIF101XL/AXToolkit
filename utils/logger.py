#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
utils/logger.py - File logging for install/remove actions
"""

import os
import logging
from datetime import datetime

LOG_DIR  = os.path.expanduser("~/.x10tools")
LOG_FILE = os.path.join(LOG_DIR, "x10tools.log")


def get_logger(name="x10tools") -> logging.Logger:
    """Return a logger that writes to ~/.x10tools/x10tools.log"""
    os.makedirs(LOG_DIR, exist_ok=True)

    logger = logging.getLogger(name)
    if logger.handlers:          # avoid duplicate handlers on re-import
        return logger

    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG)
    fmt = logging.Formatter(
        "[%(asctime)s] %(levelname)-8s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger


def get_log_path() -> str:
    return LOG_FILE
