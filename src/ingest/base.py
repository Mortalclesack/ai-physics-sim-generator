"""``IngestHandler`` protocol and shared helpers."""
from __future__ import annotations

from pathlib import Path
from typing import Protocol

from src.models.sim_spec import SimSpec


class IngestError(RuntimeError):
    """Raised when an input cannot be normalized into a SimSpec."""


class IngestHandler(Protocol):
    """Turns bytes/text at a path into a ``SimSpec``."""

    extensions: tuple[str, ...]

    def can_handle(self, path: Path) -> bool: ...

    def parse(self, path: Path, max_bytes: int) -> SimSpec: ...


def read_capped(path: Path, max_bytes: int) -> str:
    """Read a text file, refusing anything over ``max_bytes``.

    Guards against someone feeding a 4GB 'spec' and OOMing us at boot.
    """
    if not path.is_file():
        raise IngestError(f"not a file: {path}")
    size = path.stat().st_size
    if size > max_bytes:
        raise IngestError(f"{path} is {size} bytes, cap is {max_bytes}")
    return path.read_text(encoding="utf-8", errors="strict")