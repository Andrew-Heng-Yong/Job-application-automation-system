from __future__ import annotations

import threading

STOP_EVENT = threading.Event()
PAUSE_EVENT = threading.Event()


def request_stop() -> None:
    STOP_EVENT.set()


def clear_stop() -> None:
    STOP_EVENT.clear()


def is_stop_requested() -> bool:
    return STOP_EVENT.is_set()


# Pause-related API
def request_pause() -> None:
    """Set the pause flag. Callers should observe paused state via is_pause_requested()."""
    PAUSE_EVENT.set()


def clear_pause() -> None:
    """Clear the pause flag to resume operation."""
    PAUSE_EVENT.clear()


def toggle_pause() -> bool:
    """Toggle pause state. Returns True if paused after toggle."""
    if PAUSE_EVENT.is_set():
        PAUSE_EVENT.clear()
        return False
    else:
        PAUSE_EVENT.set()
        return True


def is_pause_requested() -> bool:
    return PAUSE_EVENT.is_set()
