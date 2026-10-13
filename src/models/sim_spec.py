"""``SimSpec`` — the normalized description of a simulation to generate.

An ingest handler's only job is to produce one of these. A processor's
only job is to consume one (or a ``SimFrame``) and emit another. Keeping
the boundary tight is what makes the pipeline composable.
"""
from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class Domain(str, Enum):
    RIGID_BODY = "rigid_body"
    SOFT_BODY = "soft_body"
    FLUID_SPH = "fluid_sph"
    PARTICLE_FIELD = "particle_field"


class Solver(str, Enum):
    SEMI_IMPLICIT_EULER = "semi_implicit_euler"
    RK4 = "rk4"
    VERLET = "verlet"


class SimSpec(BaseModel):
    """Normalized simulation request. Immutable after construction."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str
    domain: Domain
    solver: Solver = Solver.SEMI_IMPLICIT_EULER
    dt: float = Field(default=0.0166, gt=0.0, le=1.0)
    steps: int = Field(default=1_000, ge=1, le=10_000_000)
    seed: int = 6767
    gravity: tuple[float, float, float] = (0.0, -9.81, 0.0)
    bounds: tuple[float, float, float] = (10.0, 10.0, 10.0)
    params: dict[str, Any] = Field(default_factory=dict)

    def summary(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain.value,
            "solver": self.solver.value,
            "dt": self.dt,
            "steps": self.steps,
            "duration_s": round(self.dt * self.steps, 3),
            "seed": self.seed,
            "param_keys": ",".join(sorted(self.params)) or "-",
        }