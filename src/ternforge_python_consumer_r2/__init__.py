"""Ternforge Python Consumer R2 public API."""

__all__ = ["answer", "runtime_preview"]

from py_lib_runtime import preview_text


def answer() -> int:
    """Return the canonical answer."""
    return 42


def runtime_preview(value: str) -> str:
    """Exercise the standalone runtime dependency."""
    return preview_text(value, max_chars=32)
