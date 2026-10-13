"""Natural-language prompt -> SimSpec.

A deliberately small, offline keyword mapper. It is NOT an LLM call —
``offline=true`` is a hard default and we never phone home. It extracts
domain, step count, and a handful of params from a plain-text prompt so
users can write ``.txt`` specs without learning the JSON schema.
"""
from __future__ import annotations

import re
from pathlib import Path

from src.ingest.base import IngestError, read_capped
from src.models.sim_spec import Domain, SimSpec, Solver

_DOMAIN_HINTS: dict[Domain, tuple[str, ...]] = {
    Domain.RIGID_BODY: ("rigid", "bounce", "stack", "domino", "box"),
    Domain.SOFT_BODY: ("soft", "cloth", "jelly", "rope", "deform"),
    Domain.FLUID_SPH: ("fluid", "water", "sph", "liquid", "pour"),
    Domain.PARTICLE_FIELD: ("particle", "field", "smoke", "spark", "dust"),
}

_SOLVER_HINTS: dict[Solver, tuple[str, ...]] = {
    Solver.RK4: ("rk4", "accurate", "precise"),
    Solver.VERLET: ("verlet", "stable", "cloth"),
    Solver.SEMI_IMPLICIT_EULER: ("fast", "euler", "default"),
}


def _pick_domain(text: str) -> Domain:
    lowered = text.lower()
    for domain, hints in _DOMAIN_HINTS.items():
        if any(h in lowered for h in hints):
            return domain
    return Domain.RIGID_BODY


def _pick_solver(text: str) -> Solver:
    lowered = text.lower()
    for solver, hints in _SOLVER_HINTS.items():
        if any(h in lowered for h in hints):
            return solver
    return Solver.SEMI_IMPLICIT_EULER


def _pick_steps(text: str) -> int:
    match = re.search(r"(\d{2,7})\s*(?:steps|frames)", text, re.IGNORECASE)
    if match:
        return max(1, min(int(match.group(1)), 10_000_000))
    return 1_000


class PromptHandler:
    extensions = (".txt",)

    def can_handle(self, path: Path) -> bool:
        return path.suffix.lower() in self.extensions

    def parse(self, path: Path, max_bytes: int) -> SimSpec:
        text = read_capped(path, max_bytes).strip()
        if not text:
            raise IngestError(f"empty prompt: {path}")
        try:
            return SimSpec(
                name=path.stem,
                domain=_pick_domain(text),
                solver=_pick_solver(text),
                steps=_pick_steps(text),
                params={"prompt": text[:512]},
            )
        except Exception as exc:
            raise IngestError(f"{path} failed SimSpec validation: {exc}") from exc