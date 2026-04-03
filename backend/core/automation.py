from __future__ import annotations

import time
from pathlib import Path

import pyautogui
import pyperclip
import threading

# Use shared stop_flag implementation so the same Event is visible across modules
from backend.core.state_handler import request_stop, clear_stop, is_stop_requested

from backend.cover_letter_maker.cover_letter_maker import (
    generate_cover_letter,
    generate_cover_letter_minor_change,
)
from backend.core.helpers import (
    img,
    log,
    save_debug_screenshot,
    file_exists,
    _locate_all,
    find_center,
    wait_for_image,
    click_image,
    image_exists,
    wait_for_any_image,
    scroll_page,
    copy_all_visible_text,
    extract_between_anchors,
    latest_generated_pdf_path,
    wait_if_paused,
)
from backend.core.app_config_loader import load_app_config

# Load configuration with safe fallbacks
_cfg = {}
try:
    _cfg = load_app_config()
except Exception:
    _cfg = {}

PAGE_READY_TIMEOUT = int(_cfg.get("page_ready_timeout", 30))
POST_APPLY_TIMEOUT = int(_cfg.get("post_apply_timeout", 1))
APPLY_RETRY_COUNT = int(_cfg.get("apply_retry_count", 3))
MAX_SCROLL_PAGES = int(_cfg.get("max_scroll_pages", 20))
ROW_HALF_HEIGHT = int(_cfg.get("row_half_height", 60))
LEFT_SCAN_WIDTH_RATIO = float(_cfg.get("left_scan_width_ratio", 0.82))
START_ANCHOR = _cfg.get("start_anchor", "Job - Country:")
END_ANCHOR = _cfg.get("end_anchor", "Targeted Degrees and Disciplines:")

PREV_COMPANY_NAME: str | None = None
LAST_COVER_LETTER_PATH: Path | None = None
LAST_RESUME_VERSION_NAME: str | None = None


# -----------------------------
# Helpers used only by automation
# -----------------------------

def recover_from_stale_apply_page() -> bool:
    if not wait_if_paused():
        return False

    log("Stale page detected. Returning to search page...")

    # First try browser back (close tab)
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


# can be edited later
def row_has_target_level(region) -> bool:
    if not wait_if_paused():
        return False
    has_jr = image_exists(img("jr.png"), region=region)
    has_inter = image_exists(img("inter.png"), region=region)
    # has_sr = image_exists(img("sr.png"), region=region)
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
        if is_stop_requested():
            log("Stop requested during job search.")
            return None
        # Respect pause between pages
        if not wait_if_paused():
            return None
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
    if not wait_if_paused():
        return None

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

    if not wait_if_paused():
        raise RuntimeError("stop requested during prescreen wait")

    log("Prescreening detected. Waiting for application options page...")
    markers = [img("create_custome_package.png")]
    optional_marker = img("app_option.png")
    if file_exists(optional_marker):
        markers.insert(0, optional_marker)

    # Reduced timeout from 3600s to 10s for debugging / faster failure handling
    found = wait_for_any_image(markers, timeout=10)
    if not found:
        save_debug_screenshot("prescreen_timeout")
        raise RuntimeError("prescreen timeout")

    log("Application options page detected after prescreening.")


# -----------------------------
# Step 5
# -----------------------------
def open_quickview() -> bool:
    if not wait_if_paused():
        return False
    if not click_image(img("quick_view.png"), timeout=10):
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
    pos = wait_for_image(img("close.png"), timeout=10)
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

    # Run potentially long-running cover-letter generation in a thread with timeout
    result: dict = {}

    def _worker():
        try:
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
            result["ok"] = True
            result["resume_name"] = resume_name
            result["cover_letter_file_name"] = cover_letter_file_name
        except Exception as exc:
            result["ok"] = False
            result["error"] = exc

    if not wait_if_paused():
        raise RuntimeError("stop requested")

    log("Starting cover letter generation (may take some time)")
    save_debug_screenshot("before_generate_cover_letter")
    thread = threading.Thread(target=_worker, daemon=True)
    thread.start()

    # Wait for worker but poll so we can respond to stop requests quickly
    total_timeout = 120.0
    poll_interval = 0.5
    elapsed = 0.0
    while thread.is_alive() and elapsed < total_timeout:
        if is_stop_requested():
            log("Stop requested during cover letter generation. Aborting wait.")
            save_debug_screenshot("cover_letter_stop_requested")
            raise RuntimeError("stop requested")
        thread.join(poll_interval)
        elapsed += poll_interval

    if thread.is_alive():
        log("Cover letter generation timed out after 120s.")
        save_debug_screenshot("cover_letter_timeout")
        raise RuntimeError("cover letter generation timeout")

    if not result.get("ok"):
        err = result.get("error")
        log(f"Cover letter generation failed: {err}")
        save_debug_screenshot("cover_letter_failure")
        raise RuntimeError(f"cover letter generation error: {err}")

    resume_name = result["resume_name"]
    cover_letter_file_name = result["cover_letter_file_name"]

    cover_letter_path = latest_generated_pdf_path(cover_letter_file_name)
    PREV_COMPANY_NAME = company_name
    LAST_COVER_LETTER_PATH = cover_letter_path
    LAST_RESUME_VERSION_NAME = resume_name
    return resume_name, cover_letter_path


# -----------------------------
# Step 6
# -----------------------------
def go_to_application_options() -> bool:
    if not wait_if_paused():
        return False
    package_img = img("create_custome_package.png")
    if not click_image(package_img, timeout=10):
        save_debug_screenshot("package_click_fail")
        return False
    time.sleep(1)
    return True


def scroll_to_bottom_of_page() -> None:
    for _ in range(MAX_SCROLL_PAGES):
        scroll_page()


def upload_cover_letter(cover_letter_path: Path) -> bool:
    if not wait_if_paused():
        return False
    if not cover_letter_path.exists():
        log(f"Cover letter PDF not found: {cover_letter_path}")
        save_debug_screenshot("cover_letter_missing")
        return False

    if not click_image(img("upload_new_cover_letter.png"), timeout=10):
        save_debug_screenshot("upload_new_cover_letter_fail")
        return False
    time.sleep(0.5)

    if not click_image(img("text_bar.png"), timeout=10):
        save_debug_screenshot("text_bar_fail")
        return False
    time.sleep(0.2)

    pyperclip.copy(cover_letter_path.stem)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.1)

    if not click_image(img("upload.png"), timeout=10):
        save_debug_screenshot("upload_click_fail")
        return False
    time.sleep(0.5)

    if not click_image(img("choose_file.png"), timeout=10):
        save_debug_screenshot("choose_file_fail")
        return False
    time.sleep(1.0)

    # Select the top PDF in the file dialog and click Open (revert to clicking UI)
    if not click_image(img("pdf.png"), timeout=10):
        save_debug_screenshot("choose_pdf_fail")
        return False
    time.sleep(0.3)


def select_resume_by_name(resume_version_name: str) -> bool:
    if not wait_if_paused():
        return False
    resume_img = img(f"{resume_version_name}.png")
    if not file_exists(resume_img):
        log(f"Resume image not found: {Path(resume_img).name}")
        save_debug_screenshot("resume_image_missing")
        return False

    if not click_image(resume_img, timeout=10):
        log(f"Could not click resume image for {resume_version_name}")
        save_debug_screenshot("resume_select_fail")
        return False
    time.sleep(0.8)
    return True


def submit_application() -> bool:
    if not wait_if_paused():
        return False
    if not click_image(img("submit.png"), timeout=10):
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
    if is_stop_requested():
        log("Stop requested before processing job.")
        return False

    # Respect pause at the start of processing
    if not wait_if_paused():
        return False

    target = find_job_to_apply()
    if not target:
        return False

    page_type = click_apply_and_wait_for_next_page(target)
    if page_type is None:
        return True
    handle_prescreen_if_needed(page_type)

    if is_stop_requested():
        log("Stop requested after apply, aborting job.")
        recover_from_stale_apply_page()
        return False

    if not open_quickview():
        raise RuntimeError("quickview error")
    company_name, job_description = collect_quickview_text()
    if not close_quickview():
        raise RuntimeError("quickview close error")

    resume_version_name, cover_letter_path = generate_cover_letter_for_current_job(job_description, company_name)

    if is_stop_requested():
        log("Stop requested before uploading, aborting job.")
        return False

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
        if is_stop_requested():
            log("Stop requested. Exiting main loop.")
            break
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
