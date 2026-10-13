"""Rigid-body integrator (semi-implicit Euler by default).

N bodies under gravity with a simple axis-aligned box collision. Good
enough for stacking/bounce scenes and fast enough to run 200k steps in
a couple of seconds for n < 50.
"""
from __future__ import annotations

import numpy as np

from src.models.sim_frame import SimFrame
from src.models.sim_spec import SimSpec, Solver
from src.processors.base import ProcessorError, RunContext


class RigidBodyProcessor:
    def name(self) -> str:
        return "rigid_body"

    def validate(self, spec: SimSpec) -> None:
        if spec.domain.value != "rigid_body":
            raise ProcessorError(f"rigid_body cannot run domain {spec.domain.value}")
        n = int(spec.params.get("bodies", 8))
        if not 1 <= n <= 4096:
            raise ProcessorError(f"params.bodies={n} out of range [1, 4096]")

    def run(self, spec: SimSpec, ctx: RunContext) -> list[SimFrame]:
        n = int(spec.params.get("bodies", 8))
        masses = ctx.rng.uniform(0.5, 5.0, size=n)
        pos = ctx.rng.uniform(-2.0, 2.0, size=(n, 3))
        pos[:, 1] = ctx.rng.uniform(1.0, 5.0, size=n)
        vel = np.zeros((n, 3), dtype=np.float64)
        gravity = np.asarray(spec.gravity, dtype=np.float64)
        bounds = np.asarray(spec.bounds, dtype=np.float64)
        restitution = float(spec.params.get("restitution", 0.6))

        frames: list[SimFrame] = []
        for step in range(spec.steps):
            if spec.solver is Solver.RK4:
                # midpoint: derivative at half-step
                half = vel + 0.5 * spec.dt * gravity
                pos = pos + spec.dt * half
            else:
                pos = pos + spec.dt * vel
            vel = vel + spec.dt * gravity

            for axis in range(3):
                low = -bounds[axis]
                high = bounds[axis]
                below = pos[:, axis] < low
                above = pos[:, axis] > high
                if np.any(below) or np.any(above):
                    pos[below, axis] = low + (low - pos[below, axis]) * 0.0
                    pos[above, axis] = high - (pos[above, axis] - high) * 0.0
                    vel[below | above, axis] *= -restitution

            frames.append(SimFrame(step=step, time=step * spec.dt, positions=pos.copy(), velocities=vel.copy()))

        ctx.steps_done += spec.steps
        return frames