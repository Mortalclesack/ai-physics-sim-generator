# Contributing to ai-physics-sim-generator

Thanks for wanting to push the sim pipeline forward. This repo is a
Windows desktop tool that turns natural-language + parameter specs into
runnable physics simulations (rigid body, soft body, fluid, particle
fields) and exports them to playable artifacts.

## Dev Environment

- Windows 10/11, Python 3.12.x (3.11 works, 3.13 not yet verified)
- `python -m venv .venv && .venv\Scripts\activate`
- `pip install -e .[dev]`
- Optional native accel: MSVC 2022 + CMake 3.28 for `native/` kernels
- Optional .NET 8 SDK if you're extending the C# export bridge
- Optional JDK 17 if you're touching the Java export bridge

## Pipeline Model

Everything in this repo is a **job** moving through a **pipeline**:

```
ingest handler -> processor -> output driver
```

- **Ingest handlers** (`src/ingest/`) turn raw input (prompt, JSON spec,
  CSV params, scene description) into a normalized `SimSpec`.
- **Processors** (`src/processors/`) are pure-ish transforms over a
  `SimSpec` or `SimFrame`. They must be deterministic given a seed.
- **Output drivers** (`src/drivers/`) write artifacts: `.apsim`
  bundles, GLTF, CSV trajectories, MP4 previews, or hand off to a
  native/physics engine adapter.
- **Job utils** (`src/jobs/`) own scheduling, retries, caching, and
  telemetry.

If your change crosses more than one layer, open an issue first so we
can agree on the seam.

## Adding a Processor

1. Subclass `processors.base.Processor`.
2. Implement `name()`, `validate(spec)`, and `run(spec, ctx)`.
3. Register it in `processors.registry.REGISTRY`.
4. Add a test in `tests/` that feeds a known `SimSpec` and asserts the
   output hash. Determinism is a hard requirement.

## Adding an Output Driver

Drivers write bytes or files. If a driver touches the network, it must
go through `jobs.telemetry` and respect `config/default.toml`'s
`offline = true` default. No silent uploads, ever.

## Code Style

- `ruff` for lint + format. `mypy --strict` on `src/`.
- Type every public function. `Any` in a signature needs a comment.
- No global mutable state outside `processors.registry` and the
  driver plugin table. Both are frozen after bootstrap.

## Tests

- `pytest -q` for unit tests.
- `pytest -m integration` for end-to-end pipeline runs (slower).
- Deterministic seeds only. If a test flakes, it's a bug.

## PR Checklist

- [ ] `ruff check . && mypy src`
- [ ] `pytest -q`
- [ ] New processor/driver has a determinism test
- [ ] `CHANGELOG`-worthy change noted in PR body
- [ ] No new network calls without an offline guard

## Commit Style

`area: short imperative summary` — e.g.
`processors: add SPH fluid solver`, `drivers: fix gltf normal winding`.

## Code of Conduct

Be a decent human. We build sims, not drama.