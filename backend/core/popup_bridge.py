"""Thread-safe bridge for requesting a UI popup edit from a non-UI thread.

Automation (running in a worker thread) calls request_edit(text) which blocks
until the main UI shows a popup editor and returns the edited text.

The main window polls for requests (or could be wired to a signal) and calls
"take_request()" to retrieve the pending request, then calls
"set_response(edited_text)" to wake the waiting automation thread.

This is intentionally lightweight and uses threading.Event for synchronization.
"""
from __future__ import annotations

import threading
from typing import Optional

_request_lock = threading.Lock()
_request_text: Optional[str] = None
_response_text: Optional[str] = None
# Event set by request_edit() to indicate main thread should show dialog
_request_event = threading.Event()
# Event set by main thread when response is available
_response_event = threading.Event()


def request_edit(text: str) -> str:
    """Called from a worker thread to request a UI edit.

    Blocks until main thread sets a response via set_response().
    Returns the edited text (or original text if UI cancels).
    """
    global _request_text
    global _response_text

    with _request_lock:
        if _request_text is not None:
            raise RuntimeError("A popup edit request is already pending")
        _request_text = text
        _response_text = None
        _response_event.clear()
        _request_event.set()

    # Wait for main thread to set response
    _response_event.wait()

    with _request_lock:
        resp = _response_text if _response_text is not None else text
        # cleanup
        _request_text = None
        _response_text = None
        _request_event.clear()
        _response_event.clear()

    return resp


def has_request() -> bool:
    return _request_event.is_set()


def take_request() -> Optional[str]:
    """Called on main (UI) thread to retrieve the pending request text.

    Returns the original text or None if no request pending.
    """
    with _request_lock:
        return _request_text


def set_response(edited_text: str | None) -> None:
    """Called on main thread to set the response and wake the worker.

    If edited_text is None, the original text will be used by the worker.
    """
    global _response_text
    with _request_lock:
        _response_text = edited_text
        _response_event.set()
