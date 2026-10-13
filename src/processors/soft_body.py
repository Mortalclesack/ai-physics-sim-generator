"""Soft-body (mass-spring) processor.

A grid of point masses connected by springs, integrated with Verlet.
Stable at dt <= 1/60 for the default stiffness. Emits frames same as
every other processor.
"""
from __future__ import annotations

import numpy as np

from src.models.sim_frame import SimFrame
from src.models.sim_spec import SimSpec
from src.processors.base import ProcessorError, RunContext


class SoftBodyProcessor:
    def name(self) -> str:
        return "soft_body"

    def validate(self, spec: SimSpec)