"""Dispatch a file to the right ingest handler by extension.

This is the single entry point the CLI calls. Adding a new format means
appending a handler to ``_HANDLERS``, nothing else.
"""
from __future__ import annotations

from pathlib import Path

from src.ingest.base import IngestError, IngestHandler
from src.ingest.json_handler import JsonYamlHandler
from src.ingest.prompt_handler import PromptHandler
from src.models.sim_spec import SimSpec

_HANDLERS: tuple[IngestHandler, ...] = (
    JsonYamlHandler(),
    PromptHandler(),
)

_DEFAULT_MAX_BYTES = 8_388_608


def ingest_file(path: Path, max_bytes: int = _DEFAULT_MAX_BYTES) -> SimSpec:
    """Parse ``path`` into a ``SimSpec`` using the first capable handler."""
    resolved = path.resolve()
    for handler in _HANDLERS:
        if handler.can_handle(resolved):
            return handler.parse(resolved, max_bytes)
    exts = ", ".join(e for h in _HANDLERS for e in h.extensions)
    raise IngestError(f"no handler for {resolved.suffix!r}; supported: {exts}")