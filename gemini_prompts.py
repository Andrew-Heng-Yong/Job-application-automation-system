RESUME_SELECTION_SYSTEM_PROMPT = """You are helping choose the best resume version for a job application.
Pick exactly one resume from the provided catalog.
Prefer conservative extraction over guessing.
Return JSON only.
"""

RESUME_SELECTION_USER_PROMPT_TEMPLATE = """Job description:
{job_description}

Resume catalog:
{resume_catalog}

Tasks:
1. Select the single best resume for this job.
2. Extract the company name from the job description if it is explicitly stated.
3. Provide 3 to 6 emphasis points to use in the cover letter.

Return JSON with keys:
- selected_resume_name
"""

COVER_LETTER_SYSTEM_PROMPT = """You write concise, specific, professional cover letters.
My information: use them selectively based on the job description.
- 
-
- 

Constraints: 
- Keep word count under 150 words
- Use only the provided materials
- Do not invent experience
- Do not mention missing information
- Output only the final cover letter text
"""

COVER_LETTER_USER_PROMPT_TEMPLATE = """Write a tailored cover letter.

Company: {company_name}

Job description:
{job_description}

Selected resume name: {resume_name}
Selected resume text:
{resume_text}

Emphasis points:
{emphasis_points}
"""

MINOR_CHANGE_SYSTEM_PROMPT = """You write concise, specific, professional cover letters.
You are revising for a new role at the same company.
Keep continuity with the previous cover letter, but introduce only minor changes to fit the new job.
Avoid copying long phrases verbatim.
Use only the provided materials.
Output only the final cover letter text.
"""

MINOR_CHANGE_USER_PROMPT_TEMPLATE = """Write a tailored cover letter for a new role at the same company.

Company: {company_name}

Job description:
{job_description}

Selected resume name: {resume_name}
Selected resume text:
{resume_text}

Emphasis points:
{emphasis_points}

Use the uploaded previous cover letter PDF as context.
Preserve general tone and motivation, but make minor changes for the new role.
"""