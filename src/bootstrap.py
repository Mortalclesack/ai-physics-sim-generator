"""Entry bootstrap: wires config, registry, and pipeline for the CLI.

This is the first module touched on process start. It loads config,
freezes the processor/driver registries, and hands a ready ``Pipeline``
to the CLI. Nothing here should be imported by processors or drivers —
it's a top-of-stack module.
"""
from __future__ import annotations

import logging
import sys
from pathlib import Path

from src.config.loader import load_config
from src.config.schema import AppConfig
from src.drivers.registry import build_driver_table
from src.jobs.pipeline import Pipeline
from src.processors.registry import build_processor_table


def _configure_logging(cfg: AppConfig) -> None:
    level = getattr(logging, cfg.app.log_level.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
        stream=sys.stderr,
    )


def bootstrap(config_path: Path | None = None) -> Pipeline:
    """Load config, freeze registries, return a ready pipeline.

    Raises ``ConfigError`` if the config is malformed. Raises
    ``RegistryError`` if any processor/driver fails to register.
    """
    cfg = load_config(config_path)
    _configure_logging(cfg)
    log = logging.getLogger("apsim.bootstrap")
    log.info("booting %s v%s (offline=%s)", cfg.app.name, cfg.app.version, cfg.app.offline)

    processors = build_processor_table(cfg.processors.enabled)
    drivers = build_driver_table(cfg.drivers.enabled, allowlist=cfg.drivers.plugin_allowlist)
    log.info("registered %d processors, %d drivers", len(processors), len(drivers))

    return Pipeline(config=cfg, processors=processors, drivers=drivers)