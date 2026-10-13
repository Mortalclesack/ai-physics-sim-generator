"""``Processor`` base class and the shared run context."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

import numpy as np

from src.models.sim_frame import SimFrame
from src.models.sim_spec import SimSpec


@dataclass(slots=True)
class RunContext:
    """Mutable state carried across processors in a single job run."""

    rng: np.random.Generator
    steps_done: int = 0
    warnings: list[str] = field(default_factory=list)


class ProcessorError(RuntimeError):
    """Raised when a processor cannot complete its transform."""


class Processor(Protocol):
    """A named, deterministic transform over a SimSpec or SimFrame."""

    def name(self) -> str: ...

    def validate(self, spec: SimSpec) -> None: ...

    def run(self, spec: SimSpec, ctx: RunContext) -> list[SimFrame]: ...