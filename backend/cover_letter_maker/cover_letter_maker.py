"""Gemini cover-letter generator.

Requirements:
    pip install -U google-genai reportlab

Environment:
    Set GEMINI_API_KEY before calling either public function.

This module intentionally exposes only two public functions:
    - generate_cover_letter(job_description)
    - generate_cover_letter_minor_change(job_description, prev_cover_letter_pdf)

It is NOT this module's job to decide whether a cover letter needs a minor
or major change. The caller should pick which function to use.
"""

from __future__ import annotations

import json
import os
import re
from pathlib import Path
from typing import Any

from google import genai
from google.genai import types
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


from .gemini_config_loader import (
    API_KEY,
    MODEL_NAME,
    BASE_DIR,
    RESUME_SELECTION_SYSTEM_PROMPT,
    RESUME_SELECTION_USER_PROMPT_TEMPLATE,
    COVER_LETTER_SYSTEM_PROMPT,
    COVER_LETTER_USER_PROMPT_TEMPLATE,
    MINOR_CHANGE_SYSTEM_PROMPT,
    MINOR_CHANGE_USER_PROMPT_TEMPLATE,
    RESUME_CATALOG,
    ADDITIONAL_PERSONAL_INFORMATION,
    COVER_LETTER_WORD_LIMIT,
)


# =========================
# Internal helpers
# =========================

_SELECTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "company_name": {"type": ["string", "null"]},
        "selected_resume_name": {"type": "string"},
        "rationale": {"type": "string"},
        "emphasis_points": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "maxItems": 6,
        },
    },
    "required": [
        "company_name",
        "selected_resume_name",
        "rationale",
        "emphasis_points",
    ],
}


def _get_client() -> genai.Client:
    api_key = API_KEY
    if not api_key:
        raise RuntimeError("Missing API key. API_KEY is empty.")
    return genai.Client(api_key=api_key)


def _catalog_for_prompt() -> str:
    return json.dumps(
        [
            {"name": item["name"], "summary": item["summary"]}
            for item in RESUME_CATALOG
        ],
        ensure_ascii=False,
        indent=2,
    )


def _select_resume_and_company(client: genai.Client, job_description: str) -> dict[str, Any]:
    prompt = RESUME_SELECTION_USER_PROMPT_TEMPLATE.format(
        job_description=job_description.strip(),
        resume_catalog=_catalog_for_prompt(),
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=RESUME_SELECTION_SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_json_schema=_SELECTION_SCHEMA,
            temperature=0.1,
        ),
    )
    data = json.loads(response.text)

    selected_name = data["selected_resume_name"]
    if selected_name not in {item["name"] for item in RESUME_CATALOG}:
        raise ValueError(
            f"Gemini selected unknown resume '{selected_name}'. "
            "Update RESUME_CATALOG or tighten the prompt."
        )
    return data


def _find_resume(selected_resume_name: str) -> dict[str, str]:
    resume_file = BASE_DIR / "resume" / f"{selected_resume_name}.pdf"
    if not resume_file.exists():
        raise FileNotFoundError(f"Resume file not found: {resume_file}")
    return {"name": selected_resume_name, "summary": "", "path": str(resume_file)}


def _upload_file_and_extract_text(client: genai.Client, file_path: str | Path) -> str:
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    uploaded = client.files.upload(file=str(file_path))
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=["Extract the full readable text from this file.", uploaded],
        config=types.GenerateContentConfig(temperature=0),
    )
    return response.text.strip()


def _sanitize_filename(text: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", text.strip())
    return cleaned.strip("_") or "cover_letter"


def _save_pdf(text: str, company_name: str, resume_name: str, suffix: str) -> Path:
    # Always write output to the project-level generated_cover_letters directory
    out_dir = BASE_DIR / "generated_cover_letters"
    out_dir.mkdir(parents=True, exist_ok=True)

    company_slug = _sanitize_filename(company_name or "unknown_company")
    resume_slug = _sanitize_filename(resume_name)
    output_path = out_dir / f"{company_slug}_{resume_slug}_{suffix}.pdf"

    styles = getSampleStyleSheet()
    normal = styles["Normal"]
    story = []

    for paragraph in [p.strip() for p in text.split("\n\n") if p.strip()]:
        story.append(Paragraph(paragraph.replace("\n", "<br/>"), normal))
        story.append(Spacer(1, 12))

    doc = SimpleDocTemplate(str(output_path), pagesize=LETTER)
    doc.build(story)
    return output_path


def _generate_letter_text(
    client: genai.Client,
    *,
    job_description: str,
    company_name: str,
    resume_name: str,
    resume_text: str,
    emphasis_points: list[str],
) -> str:
    prompt = COVER_LETTER_USER_PROMPT_TEMPLATE.format(
        company_name=company_name or "Unknown company",
        job_description=job_description.strip(),
        resume_name=resume_name,
        resume_text=resume_text,
        emphasis_points="\n".join(f"- {point}" for point in emphasis_points),
    )
    # Append additional personal information and word limit instructions for new letters
    if ADDITIONAL_PERSONAL_INFORMATION:
        prompt += "\n\nAdditional personal information:\n" + ADDITIONAL_PERSONAL_INFORMATION
    if COVER_LETTER_WORD_LIMIT:
        prompt += f"\n\nPlease keep the cover letter within {COVER_LETTER_WORD_LIMIT} words."
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=COVER_LETTER_SYSTEM_PROMPT,
            temperature=0.4,
        ),
    )
    text = response.text.strip()
    return text


def _generate_minor_change_letter_text(
    client: genai.Client,
    *,
    job_description: str,
    company_name: str,
    resume_name: str,
    resume_text: str,
    emphasis_points: list[str],
    prev_cover_letter_pdf: str | Path,
) -> str:
    previous_cover_letter_file = client.files.upload(file=str(prev_cover_letter_pdf))
    prompt = MINOR_CHANGE_USER_PROMPT_TEMPLATE.format(
        company_name=company_name or "Unknown company",
        job_description=job_description.strip(),
        resume_name=resume_name,
        resume_text=resume_text,
        emphasis_points="\n".join(f"- {point}" for point in emphasis_points),
    )
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[prompt, previous_cover_letter_file],
        config=types.GenerateContentConfig(
            system_instruction=MINOR_CHANGE_SYSTEM_PROMPT,
            temperature=0.35,
        ),
    )
    return response.text.strip()


# =========================
# Public functions
# =========================


def generate_cover_letter(job_description: str, company_name: str | None = None) -> tuple[str, str]:
    """Select a resume, generate a new cover letter, save it as a PDF.

    The caller may provide company_name to avoid relying on model extraction.

    Returns:
        (used_resume_name, cover_letter_file_name)
    """
    client = _get_client()
    selection = _select_resume_and_company(client, job_description)

    resume_name = selection["selected_resume_name"]
    # Prefer caller-provided company_name when available.
    company = (company_name or selection.get("company_name") or "Unknown company").strip()
    emphasis_points = selection["emphasis_points"]

    resume_info = _find_resume(resume_name)
    resume_text = _upload_file_and_extract_text(client, resume_info["path"])

    cover_letter_text = _generate_letter_text(
        client,
        job_description=job_description,
        company_name=company,
        resume_name=resume_name,
        resume_text=resume_text,
        emphasis_points=emphasis_points,
    )

    output_path = _save_pdf(
        text=cover_letter_text,
        company_name=company,
        resume_name=resume_name,
        suffix="cover_letter",
    )
    return resume_name, output_path.name



def generate_cover_letter_minor_change(
    job_description: str,
    prev_cover_letter_pdf: str | Path,
    company_name: str | None = None,
) -> tuple[str, str]:
    """Select a resume, revise using the previous cover letter PDF, save as a PDF.

    The caller may provide company_name to avoid relying on model extraction.

    Returns:
        (used_resume_name, cover_letter_file_name)
    """
    client = _get_client()
    selection = _select_resume_and_company(client, job_description)

    resume_name = selection["selected_resume_name"]
    # Prefer caller-provided company_name when available.
    company = (company_name or selection.get("company_name") or "Unknown company").strip()
    emphasis_points = selection["emphasis_points"]

    resume_info = _find_resume(resume_name)
    resume_text = _upload_file_and_extract_text(client, resume_info["path"])

    cover_letter_text = _generate_minor_change_letter_text(
        client,
        job_description=job_description,
        company_name=company,
        resume_name=resume_name,
        resume_text=resume_text,
        emphasis_points=emphasis_points,
        prev_cover_letter_pdf=prev_cover_letter_pdf,
    )

    output_path = _save_pdf(
        text=cover_letter_text,
        company_name=company,
        resume_name=resume_name,
        suffix="cover_letter_minor_change",
    )
    return resume_name, output_path.name
