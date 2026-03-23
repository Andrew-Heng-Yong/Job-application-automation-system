from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

RESUME_CATALOG: list[dict[str, str]] = [
    {
        "name": "general",
        "summary": "General software, programming, analytics, and broad technical experience.",
        "path": str(BASE_DIR / "resume" / "general.pdf"),
    },
    {
        "name": "software_dev",
        "summary": "Software development, coding, implementation, debugging, and developer workflows.",
        "path": str(BASE_DIR / "resume" / "software_dev.pdf"),
    },
]