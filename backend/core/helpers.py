from __future__ import annotations

import time
from datetime import datetime
from pathlib import Path

import pyautogui
import pyperclip

from .app_config_loader import load_app_config
# check stop flag to make helpers responsive
from .stop_flag import is_stop_requested

# Default image/confidence settings (will be overridden by config if provided)
_cfg = {}
try:
    _cfg = load_app_config()
except Exception:
    # fall back to defaults if config not found
    _cfg = {}

CONFIDENCE = float(_cfg.get("confidence", 0.85))
CHECK_INTERVAL = float(_cfg.get("check_interval", 0.35))
DEFAULT_TIMEOUT = float(_cfg.get("default_timeout", 10))
SCROLL_STEP = int(_cfg.get("scroll_step", -700))

BASE_DIR = Path(__file__).resolve().parent.parent.parent
IMG_DIR = BASE_DIR / "imgs"
OUTPUT_DIR = Path(BASE_DIR) / "generated_cover_letters"

def img(name: str) -> str:
    return str(IMG_DIR / name)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


# Logging sink for UI integration (callable that accepts a single str)
_LOG_SINK = None

def set_log_sink(callback):
    """Register a callable to receive formatted log messages.

    The callback will be called with a single string argument. It should be
    thread-safe — the UI will typically re-emit via a Qt signal.
    """
    global _LOG_SINK
    _LOG_SINK = callback


def log(msg: str) -> None:
    """Log a message to console and to the registered log sink (if any).

    Messages keep the existing timestamp format so callers in automation do
    not need to change.
    """
    formatted = f"[{time.strftime('%H:%M:%S')}] {msg}"

    if _LOG_SINK is not None:
        try:
            _LOG_SINK(formatted)
        except Exception:
            # Sink must not be allowed to raise into automation
            pass


def save_debug_screenshot(prefix: str = "debug") -> str:
    path = BASE_DIR / f"debug_screenshots/{prefix}_{timestamp()}.png"
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
        if is_stop_requested():
            log("Stop requested during wait_for_image; aborting wait")
            return None
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
        if is_stop_requested():
            log("Stop requested during wait_for_any_image; aborting wait")
            return None
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
