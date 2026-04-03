import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

with open(BASE_DIR / "gemini_config.json", "r", encoding="utf-8") as f:
    _cfg = json.load(f)

API_KEY = _cfg.get("API_KEY")
MODEL_NAME = _cfg.get("MODEL_NAME")

RESUME_SELECTION_SYSTEM_PROMPT = _cfg.get("RESUME_SELECTION_SYSTEM_PROMPT")
RESUME_SELECTION_USER_PROMPT_TEMPLATE = _cfg.get("RESUME_SELECTION_USER_PROMPT_TEMPLATE")
COVER_LETTER_SYSTEM_PROMPT = _cfg.get("COVER_LETTER_SYSTEM_PROMPT")
COVER_LETTER_USER_PROMPT_TEMPLATE = _cfg.get("COVER_LETTER_USER_PROMPT_TEMPLATE")
MINOR_CHANGE_SYSTEM_PROMPT = _cfg.get("MINOR_CHANGE_SYSTEM_PROMPT")
MINOR_CHANGE_USER_PROMPT_TEMPLATE = _cfg.get("MINOR_CHANGE_USER_PROMPT_TEMPLATE")

ADDITIONAL_PERSONAL_INFORMATION = _cfg.get("ADDITIONAL_PERSONAL_INFORMATION")
COVER_LETTER_WORD_LIMIT = int(_cfg.get("COVER_LETTER_WORD_LIMIT", 150))

RESUME_CATALOG = [
    {"name": item["name"], "summary": item["summary"]}
    for item in _cfg.get("RESUME_CATALOG", [])
]

print(f"API key: {API_KEY}")