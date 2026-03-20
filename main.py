from __future__ import annotations

import re
import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip

from gemini_cover_letter import (
    OUTPUT_DIR,
    generate_cover_letter,
    generate_cover_letter_minor_change,
)

# -----------------------------
# Basic settings
# -----------------------------
pyautogui.PAUSE = 0.25
pyautogui.FAILSAFE = True  # move mouse to top-left corner to stop immediately

BASE_DIR = Path(__file__).resolve().parent
IMG_DIR = BASE_DIR / "imgs"
OUTPUT_DIR = Path(OUTPUT_DIR)

CONFIDENCE = 0.85
CHECK_INTERVAL = 0.35
DEFAULT_TIMEOUT = 10
PAGE_READY_TIMEOUT = 30
POST_APPLY_TIMEOUT = 1
APPLY_RETRY_COUNT = 3
MAX_SCROLL_PAGES = 20
SCROLL_STEP = -700
ROW_HALF_HEIGHT = 60
LEFT_SCAN_WIDTH_RATIO = 0.82  # left part of row contains level tags, not the apply button

# quickview extraction anchors
START_ANCHOR = "Job - Country:"
END_ANCHOR = "Targeted Degrees and Disciplines:"

PREV_COMPANY_NAME: str | None = None
LAST_COVER_LETTER_PATH: Path | None = None
LAST_RESUME_VERSION_NAME: str | None = None


# -----------------------------
# Helpers
# -----------------------------
def img(name: str) -> str:
    return str(IMG_DIR / name)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}")


def save_debug_screenshot(prefix: str = "debug") -> str:
    path = BASE_DIR / f"{prefix}_{timestamp()}.png"
    pyautogui.screenshot(str(path))
    log(f"Saved screenshot: {path.name}")
    return str(path)


def file_exists(path: str | Path) -> bool:
    return Path(path).exists()


def _locate_center(image_path: str, confidence: float = CONFIDENCE, region=None):
    try:
        return pyautogui.locateCenterOnScreen(image_path, confidence=confidence, region=region)
    except Exception as exc:
        log(f"did not see {Path(image_path).name}: {exc}")
        return None


def _locate_all(image_path: str, confidence: float = CONFIDENCE, region=None):
    try:
        return list(pyautogui.locateAllOnScreen(image_path, confidence=confidence, region=region))
    except Exception as exc:
        log(f"Error while searching all for {Path(image_path).name}: {exc}")
        return []


def find_center(image_path: str, confidence: float = CONFIDENCE, region=None):
    return _locate_center(image_path, confidence=confidence, region=region)


def wait_for_image(image_path: str, timeout: float = DEFAULT_TIMEOUT, confidence: float = CONFIDENCE, region=None):
    start = time.time()
    while time.time() - start < timeout:
        pos = find_center(image_path, confidence=confidence, region=region)
        if pos:
            return pos
        time.sleep(CHECK_INTERVAL)
    return None


def click_image(
    image_path: str,
    timeout: float = DEFAULT_TIMEOUT,
    confidence: float = CONFIDENCE,
    clicks: int = 1,
    interval: float = 0.1,
    button: str = "left",
    region=None,
) -> bool:
    pos = wait_for_image(image_path, timeout=timeout, confidence=confidence, region=region)
    if not pos:
        log(f"Could not find image: {Path(image_path).name}")
        return False

    pyautogui.click(pos.x, pos.y, clicks=clicks, interval=interval, button=button)
    log(f"Clicked: {Path(image_path).name} at ({pos.x}, {pos.y})")
    return True


def image_exists(image_path: str, confidence: float = CONFIDENCE, region=None) -> bool:
    return find_center(image_path, confidence=confidence, region=region) is not None


def wait_for_any_image(image_paths: list[str], timeout: float, confidence: float = CONFIDENCE):
    start = time.time()
    while time.time() - start < timeout:
        for image_path in image_paths:
            if file_exists(image_path) and image_exists(image_path, confidence=confidence):
                return image_path
        time.sleep(CHECK_INTERVAL)
    return None


def scroll_page() -> None:
    pyautogui.scroll(SCROLL_STEP)
    time.sleep(0.8)


def copy_all_visible_text() -> str:
    pyperclip.copy("")
    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.6)
    return pyperclip.paste()


def extract_between_anchors(text: str, start_anchor: str, end_anchor: str) -> str | None:
    start_idx = text.find(start_anchor)
    if start_idx == -1:
        return None
    end_idx = text.find(end_anchor, start_idx)
    if end_idx == -1:
        return None
    return text[start_idx:end_idx].strip()


def latest_generated_pdf_path(file_name: str) -> Path:
    return OUTPUT_DIR / file_name


def press_enter() -> None:
    pyautogui.press("enter")
    time.sleep(1.0)

def recover_from_stale_apply_page() -> bool:
    log("Stale page detected. Returning to search page...")

    # First try browser back
    pyautogui.hotkey("ctrl", "w")
    time.sleep(1.5)

    if image_exists(img("ww_home_bar.png")):
        log("Returned to search page with Control+W.")
        return True

    # Fallback: escape
    pyautogui.press("esc")
    time.sleep(1.0)

    if image_exists(img("ww_home_bar.png")):
        log("Returned to search page with Esc.")
        return True

    save_debug_screenshot("stale_page_recovery_fail")
    log("Could not recover to search page.")
    return False
# -----------------------------
# Page checks
# -----------------------------
def wait_until_search_page_ready() -> bool:
    log("Waiting for search page...")
    ready = wait_for_image(img("ww_home_bar.png"), timeout=PAGE_READY_TIMEOUT)
    if not ready:
        log("ww_home_bar.png not found. Stopping.")
        save_debug_screenshot("job_search_not_ready")
        return False
    log("ready.")
    return True


def row_region_from_box(box):
    screen_w, screen_h = pyautogui.size()
    row_top = max(0, box.top - ROW_HALF_HEIGHT)
    row_bottom = min(screen_h, box.top + box.height + ROW_HALF_HEIGHT)
    row_height = max(1, row_bottom - row_top)
    row_width = int(screen_w * LEFT_SCAN_WIDTH_RATIO)
    return 0, row_top, row_width, row_height

#can be edited later
def row_has_target_level(region) -> bool:
    has_jr = image_exists(img("jr.png"), region=region)
    has_inter = image_exists(img("inter.png"), region=region)
    #has_sr = image_exists(img("sr.png"), region=region)
    return has_jr or has_inter


# -----------------------------
# Job selection
# -----------------------------
def find_best_apply_on_current_view():
    apply_boxes = _locate_all(img("apply.png"))
    if not apply_boxes:
        return None

    apply_boxes.sort(key=lambda b: (b.top, b.left))

    for box in apply_boxes:
        region = row_region_from_box(box)
        if row_has_target_level(region):
            center_x = box.left + box.width // 2
            center_y = box.top + box.height // 2
            log(f"Eligible job found at row y={center_y}")
            return center_x, center_y
    return None


def find_job_to_apply():
    for page_idx in range(MAX_SCROLL_PAGES):
        target = find_best_apply_on_current_view()
        if target:
            return target
        log(f"No eligible job in current view. Scrolling... ({page_idx + 1}/{MAX_SCROLL_PAGES})")
        scroll_page()

    log("no jobs aval")
    return None


# -----------------------------
# Apply flow
# -----------------------------
def click_apply_and_wait_for_next_page(apply_pos) -> str | None:
    next_markers = [img("psq.png")]
    optional_marker = img("app_option.png")
    if file_exists(optional_marker):
        next_markers.append(optional_marker)
    next_markers.append(img("create_custome_package.png"))

    pyautogui.click(apply_pos[0], apply_pos[1])
    log("Clicked apply (attempt 1)")
    time.sleep(1.0)

    for check_idx in range(1, 6):
        found = wait_for_any_image(next_markers, timeout=POST_APPLY_TIMEOUT)
        if found:
            if found.endswith("psq.png"):
                return "psq"
            return "app_options"

        log(f"Post-apply page check failed ({check_idx}/5)")

    log("Stale page after apply.")
    recover_from_stale_apply_page()
    return None


def handle_prescreen_if_needed(page_type: str) -> None:
    if page_type != "psq":
        return

    log("Prescreening detected. Waiting for application options page...")
    markers = [img("create_custome_package.png")]
    optional_marker = img("app_option.png")
    if file_exists(optional_marker):
        markers.insert(0, optional_marker)

    found = wait_for_any_image(markers, timeout=3600)
    if not found:
        save_debug_screenshot("prescreen_timeout")
        raise RuntimeError("prescreen timeout")

    log("Application options page detected after prescreening.")


# -----------------------------
# Step 5
# -----------------------------
def open_quickview() -> bool:
    if not click_image(img("quick_view.png"), timeout=DEFAULT_TIMEOUT):
        log("Could not click quick_view.png")
        save_debug_screenshot("quickview_click_fail")
        return False
    time.sleep(1)
    return True


def collect_quickview_text() -> str:
    screen_w, screen_h = pyautogui.size()
    pyautogui.click(screen_w // 2, screen_h // 2)
    time.sleep(0.3)

    raw_text = copy_all_visible_text()
    job_descripton = extract_between_anchors(raw_text, START_ANCHOR, END_ANCHOR)
    if job_descripton is None:
        save_debug_screenshot("quickview_anchor_missing")
        raise RuntimeError("quickview anchor missing")
    company_name = extract_between_anchors(raw_text, "Organization:", "Division:")
    if company_name is None:
        save_debug_screenshot("company name problems")
        raise RuntimeError("company name problems")
    # Return both raw captured text and the extracted job snippet
    return company_name, job_descripton


def close_quickview() -> bool:
    pos = wait_for_image(img("close.png"), timeout=DEFAULT_TIMEOUT)
    if not pos:
        log("Could not find close.png")
        save_debug_screenshot("close_quickview_fail")
        return False

    x, y = pos.x, pos.y
    pyautogui.click(x, y)
    time.sleep(0.5)
    pyautogui.click(x, y)
    time.sleep(0.5)
    return True


def generate_cover_letter_for_current_job(job_snippet: str, raw_quickview_text: str) -> tuple[str, Path]:
    global PREV_COMPANY_NAME, LAST_COVER_LETTER_PATH, LAST_RESUME_VERSION_NAME

    # Extract company name between Organization: and Division: from the raw quickview
    company_name = raw_quickview_text or "Unknown company"

    if PREV_COMPANY_NAME == company_name and LAST_COVER_LETTER_PATH is not None:
        resume_name, cover_letter_file_name = generate_cover_letter_minor_change(
            job_snippet,
            LAST_COVER_LETTER_PATH,
            company_name=company_name,
        )
    else:
        resume_name, cover_letter_file_name = generate_cover_letter(
            job_snippet,
            company_name=company_name,
        )

    cover_letter_path = latest_generated_pdf_path(cover_letter_file_name)
    PREV_COMPANY_NAME = company_name
    LAST_COVER_LETTER_PATH = cover_letter_path
    LAST_RESUME_VERSION_NAME = resume_name
    return resume_name, cover_letter_path


# -----------------------------
# Step 6
# -----------------------------
def go_to_application_options() -> bool:
    package_img = img("create_custome_package.png")
    if not click_image(package_img, timeout=DEFAULT_TIMEOUT):
        log("Could not click create_custome_package.png")
        save_debug_screenshot("package_click_fail")
        return False
    time.sleep(1)
    return True


def scroll_to_bottom_of_page() -> None:
    for _ in range(MAX_SCROLL_PAGES):
        scroll_page()


def upload_cover_letter(cover_letter_path: Path) -> bool:
    if not cover_letter_path.exists():
        log(f"Cover letter PDF not found: {cover_letter_path}")
        save_debug_screenshot("cover_letter_missing")
        return False

    if not click_image(img("upload_new_cover_letter.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("upload_new_cover_letter_fail")
        return False
    time.sleep(0.5)

    if not click_image(img("text_bar.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("text_bar_fail")
        return False
    time.sleep(0.3)

    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(cover_letter_path.stem)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    if not click_image(img("upload.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("upload_click_fail")
        return False
    time.sleep(0.5)

    if not click_image(img("choose_file.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("choose_file_fail")
        return False
    time.sleep(1.0)

    # Select the top PDF in the file dialog and click Open (revert to clicking UI)
    if not click_image(img("pdf.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("choose_pdf_fail")
        return False
    time.sleep(0.3)

    if not click_image(img("open.png"), timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("open_click_fail")
        return False
    time.sleep(6.0)

    upload_document_img = img("upload_a_document.png")
    if not click_image(upload_document_img, timeout=DEFAULT_TIMEOUT):
        save_debug_screenshot("upload_document_fail")
        return False
    time.sleep(1.0)
    return True


def select_resume_by_name(resume_version_name: str) -> bool:
    resume_img = img(f"{resume_version_name}.png")
    if not file_exists(resume_img):
        log(f"Resume image not found: {Path(resume_img).name}")
        save_debug_screenshot("resume_image_missing")
        return False

    if not click_image(resume_img, timeout=DEFAULT_TIMEOUT):
        log(f"Could not click resume image for {resume_version_name}")
        save_debug_screenshot("resume_select_fail")
        return False
    time.sleep(0.8)
    return True


def submit_application() -> bool:
    if not click_image(img("submit.png"), timeout=DEFAULT_TIMEOUT):
        log("Could not click submit.png")
        save_debug_screenshot("submit_click_fail")
        return False
    time.sleep(1)
    return True


# -----------------------------
# Step 7
# -----------------------------
def finish_application() -> None:
    if image_exists(img("confirm.png")):
        log("Confirm detected.")
        click_image(img("done.png"), timeout=5)
        time.sleep(1)
# -----------------------------
# Main loop
# -----------------------------
def process_one_job() -> bool:
    target = find_job_to_apply()
    if not target:
        return False

    page_type = click_apply_and_wait_for_next_page(target)
    if page_type is None:
        return True
    handle_prescreen_if_needed(page_type)

    if not open_quickview():
        raise RuntimeError("quickview error")
    company_name, job_description = collect_quickview_text()
    if not close_quickview():
        raise RuntimeError("quickview close error")

    resume_version_name, cover_letter_path = generate_cover_letter_for_current_job(job_description, company_name)

    if not go_to_application_options():
        raise RuntimeError("application options error")
    scroll_to_bottom_of_page()
    if not upload_cover_letter(cover_letter_path):
        raise RuntimeError("cover letter upload error")
    if not select_resume_by_name(resume_version_name):
        raise RuntimeError("resume select error")
    if not submit_application():
        raise RuntimeError("submit error")

    finish_application()
    return True


def main() -> None:
    log("activated!")
    time.sleep(5)

    if not wait_until_search_page_ready():
        return

    while True:
        try:
            did_work = process_one_job()
        except RuntimeError as exc:
            log(str(exc))
            break

        if not did_work:
            break

        if not wait_until_search_page_ready():
            break

    log("Bot finished.")


if __name__ == "__main__":
    main()
