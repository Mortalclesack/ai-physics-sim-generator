"""``SimFrame`` — one timestep of simulation state.

Kept as plain numpy for the hot path. A frame is: step index, time,
positions, velocities. Processors append frames; drivers serialize
them.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass(slots=True)
class SimFrame:
    step: int
    time: float
    positions: NDArray[np.float64]  # shape (n_bodies, 3)
    velocities: NDArray[np.float64]  # shape (n_bodies, 3)

    def __post_init__(self) -> None:
        if self.positions.shape != self.velocities.shape:
            raise ValueError(
                f"positions {self.positions.shape} != velocities {self.velocities.shape}"
            )
        if self.positions.ndim != 2 or self.positions.shape[1] != 3:
            raise ValueError(f"expected (n,3) arrays, got {self.positions.shape}")

    @property
    def n_bodies(self) -> int:
        return int(self.positions.shape[0])

    def kinetic_energy(self, masses: NDArray[np.float64]) -> float:
        """Sum of 0.5*m*v^2 across bodies. ``masses`` must be shape (n_bodies,)."""
        if masses.shape != (self.n_bodies,):
            raise ValueError(f"masses shape {masses.shape} != ({self.n_bodies},)")
        return float(0.5 * np.sum(masses * np.sum(self.velocities**2, axis=1)))