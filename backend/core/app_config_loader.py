from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

def load_app_config() -> dict:
    path = BASE_DIR / "app_config.json"
    if not path.exists():
        raise FileNotFoundError(f"Missing app configuration: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
