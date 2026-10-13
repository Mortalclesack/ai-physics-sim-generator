"""JSON / YAML spec ingest handler."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from src.ingest.base import IngestError, read_capped
from src.models.sim_spec import SimSpec


class JsonYamlHandler:
    extensions = (".json", ".yaml", ".yml")

    def can_handle(self, path: Path) -> bool:
        return path.suffix.lower() in self.extensions

    def parse(self, path: Path, max_bytes: int) -> SimSpec:
        text = read_capped(path, max_bytes)
        try:
            raw = json.loads(text) if path.suffix.lower() == ".json" else yaml.safe_load(text)
        except (json.JSONDecodeError, yaml.YAMLError) as exc:
            raise IngestError(f"cannot parse {path}: {exc}") from exc
        if not isinstance(raw, dict):
            raise IngestError(f"{path} must contain a mapping, got {type(raw).__name__}")
        if "name" not in raw:
            raw["name"] = path.stem
        try:
            return SimSpec.model_validate(raw)
        except Exception as exc:
            raise IngestError(f"{path} failed SimSpec validation: {exc}") from exc