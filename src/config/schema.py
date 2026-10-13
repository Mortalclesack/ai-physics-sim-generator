"""Pydantic models describing the runtime config surface.

Every section in ``config/default.toml`` maps to a model here. Unknown
keys are rejected so a typo in config fails loudly at boot, not at
step 40k of a sim.
"""
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class AppSection(_Strict):
    name: str
    version: str
    offline: bool = True
    workspace_root: str = "workspace"
    log_level: str = "info"


class PipelineSection(_Strict):
    max_steps: int = Field(default=200_000, ge=1, le=10_000_000)
    default_dt: float = Field(default=0.0166, gt=0.0, le=1.0)
    seed: int = 6767
    worker_threads: int = Field(default=4, ge=1, le=64)
    cache_dir: str = ".apcache"


class IngestSection(_Strict):
    accept_extensions: list[str]
    max_spec_bytes: int = Field(default=8_388_608, ge=1024)


class ProcessorsSection(_Strict):
    enabled: list[str]
    default_solver: str = "semi_implicit_euler"


class DriversSection(_Strict):
    enabled: list[str]
    plugin_allowlist: list[str] = Field(default_factory=list)
    output_root: str = "sim_outputs"


class TelemetrySection(_Strict):
    enabled: bool = False
    endpoint: str = ""


class SecuritySection(_Strict):
    allow_eval: bool = False
    sandbox_writes: bool = True
    max_ingest_depth: int = Field(default=6, ge=1, le=32)


class AppConfig(_Strict):
    app: AppSection
    pipeline: PipelineSection
    ingest: IngestSection
    processors: ProcessorsSection
    drivers: DriversSection
    telemetry: TelemetrySection
    security: SecuritySection