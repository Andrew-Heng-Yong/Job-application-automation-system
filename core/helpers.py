from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip

# Default image/confidence settings (can be overridden in caller if needed)
CONFIDENCE = 0.85
CHECK_INTERVAL = 0.35
DEFAULT_TIMEOUT = 10
SCROLL_STEP = -700

BASE_DIR = Path(__file__).resolve().parent.parent
IMG_DIR = BASE_DIR / "imgs"
OUTPUT_DIR = Path(BASE_DIR) / "generated_cover_letters"

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


def wait_for_any_image(image_paths: list[str], timeout: float = DEFAULT_TIMEOUT, confidence: float = CONFIDENCE):
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
