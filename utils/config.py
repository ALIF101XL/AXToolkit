#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
utils/config.py - Persistent JSON config for user preferences
Stored at ~/.x10tools/config.json
"""

import os
import json

CONFIG_DIR  = os.path.expanduser("~/.x10tools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULTS = {
    "auto_update_on_add_repo": False,
    "confirm_before_install": True,
    "log_enabled": True,
    "theme": "dark",
}


class Config:
    def __init__(self):
        self._data = {}
        self._load()

    def _load(self):
        os.makedirs(CONFIG_DIR, exist_ok=True)
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE) as f:
                    self._data = json.load(f)
            except Exception:
                self._data = {}
        # Fill missing keys with defaults
        for k, v in DEFAULTS.items():
            self._data.setdefault(k, v)

    def save(self):
        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(self._data, f, indent=2)
            return True
        except Exception:
            return False

    def get(self, key, fallback=None):
        return self._data.get(key, fallback)

    def set(self, key, value):
        self._data[key] = value
        self.save()

    def all(self) -> dict:
        return dict(self._data)

    def reset(self):
        self._data = dict(DEFAULTS)
        self.save()
