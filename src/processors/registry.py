"""Frozen registry of available processors.

Built once at bootstrap. After ``build_processor_table`` returns, the
table is a ``MappingProxyType`` — processors cannot be added at runtime,
which keeps determinism auditable.
"""
from __future__ import annotations

from types import MappingProxyType
from typing import Mapping

from src.processors.base import Processor, ProcessorError
from src.processors.fluid_sph import FluidSphProcessor
from src.processors.particle_field import ParticleFieldProcessor
from src.processors.rigid_body import RigidBodyProcessor
from src.processors.soft_body import SoftBodyProcessor

_CATALOG: dict[str, type[Processor]] = {
    "rigid_body": RigidBodyProcessor,
    "soft_body": SoftBodyProcessor,
    "fluid_sph": FluidSphProcessor,
    "particle_field": ParticleFieldProcessor,
}


def build_processor_table(enabled: list[str]) -> Mapping[str, Processor]:
    """Instantiate the enabled processors and freeze the table."""
    table: dict[str, Processor] = {}
    for key in enabled:
        cls = _CATALOG.get(key)
        if cls is None:
            raise ProcessorError(f"unknown processor {key!r}; known: {sorted(_CATALOG)}")
        table[key] = cls()
    return MappingProxyType(table)