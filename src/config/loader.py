"""Load and validate ``config/default.toml`` into an ``AppConfig``.

Layered resolution order (later wins):
  1. packaged ``config/default.toml``
  2. user-provided path (if given)
  3. ``APSIM_*`` environment overrides
"""
from __future__ import annotations

import os
import tomllib
from pathlib import Path
from typing import Any

from src.config.schema import AppConfig

_REPO_ROOT = Path(__file__).resolve().parents[2]
_DEFAULT_CONFIG = _REPO_ROOT / "config" / "default.toml"


class ConfigError(RuntimeError):
    """Raised when config is missing, malformed, or fails schema validation."""


def _read_toml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise ConfigError(f"config not found: {path}")
    try:
        with path.open("rb") as fh:
            return tomllib.load(fh)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigError(f"malformed TOML in {path}: {exc}") from exc


def _coerce(value: str) -> Any:
    lowered = value.strip().lower()
    if lowered in {"true", "false"}:
        return lowered == "true"
    try:
        return int(value)
    except ValueError:
        pass
    try:
        return float(value)
    except ValueError:
        pass
    return value


def _apply_env_overrides(raw: dict[str, Any], prefix: str = "APSIM_") -> dict[str, Any]:
    for key, value in os.environ.items():
        if not key.startswith(prefix):
            continue
        parts = key[len(prefix):].lower().split("_", 1)
        if len(parts) != 2:
            continue
        section, field = parts
        raw.setdefault(section, {})[field] = _coerce(value)
    return raw


def load_config(path: Path | None = None) -> AppConfig:
    """Resolve, merge, and validate the config. Returns a frozen ``AppConfig``."""
    raw = _read_toml(_DEFAULT_CONFIG)
    if path is not None:
        user = _read_toml(path)
        for section, values in user.items():
            raw.setdefault(section, {}).update(values)
    raw = _apply_env_overrides(raw)
    try:
        return AppConfig.model_validate(raw)
    except Exception as exc:  # pydantic ValidationError
        raise ConfigError(f"config failed validation: {exc}") from exc