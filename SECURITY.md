# Security Policy

## Scope

`ai-physics-sim-generator` is a **local desktop tool**. It reads spec
files, runs simulations, and writes output artifacts. It is not a
service and does not listen on any port by default.

## Threat Model

Things we care about:

- **Malicious spec files.** `.apsim` bundles and CSV param files are
  parsed by `ingest.*` handlers. Parsers must be fuzzed and must never
  `eval()` or `exec()` spec content. If you find an ingest path that
  executes input, that's a critical bug.
- **Plugin drivers.** Third-party output drivers are loaded from
  `drivers/plugins/`. They run in-process. A hostile driver is a
  hostile process — only install drivers you trust. We sandbox
  plugin imports behind an explicit allowlist in
  `config/default.toml`.
- **Native kernels.** `native/` C++ code is compiled locally. If you
  distribute prebuilt `.pyd` files, sign them.
- **Path traversal on export.** Output drivers must refuse to write
  outside the configured `workspace/` root. Report any bypass.
- **Prompt-injection via ingested text.** The NL ingest handler treats
  prompts as data, never as instructions to the tool itself. If you
  find a path where a prompt steers the pipeline, that's a bug.

## Out of Scope

- Denial of service from intentionally huge simulations. Cap your
  `max_steps` in config.
- Local privilege escalation via already-compromised user account.

## Reporting a Vulnerability

Email `security@ai-physics-sim-generator.dev` with:

1. Affected version (`ai-physics-sim-generator --version`).
2. Minimal repro (spec file + command).
3. Impact statement.
4. Whether you want credit.

We aim to acknowledge within 72 hours and ship a fix within 14 days
for critical issues. Coordinated disclosure: 90 days or a fix,
whichever comes first.

## Hardening Defaults

- `offline = true` — no network by design.
- `max_steps = 200_000` — runaway sim guard.
- `plugin_allowlist = []` — empty by default.
- `workspace_root` — sandboxed writes.

## Supported Versions

| Version | Supported |
|---------|-----------|
| 0.9.x   | yes       |
| 0.8.x   | security-only |
| < 0.8   | no        |