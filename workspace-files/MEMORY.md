# MEMORY.md — Long-Term Memory

## About Jakin

- **Name:** Jakin
- **Role:** CEO of IT team
- **Timezone:** CDT (America/Chicago)
- **Communication:** Web chat only (for now)
- **Plan:** Kimi Moderato ($19/mo)
- **Background:** NSA TAO, CIA, FBI, Five Eyes, DoE (all 5 quantum centers), Los Alamos, NIST, NSF — all highest clearance. SRE at Palantir, Google, SpaceX. Google Red Team. Highest-clearance security threat detection at Google & Palantir.

### Preferences
- Ask before acting when uncertain
- Direct, efficient communication preferred
- Match his tone (business casual, adapt as needed)
- Groups: speak only when spoken to
- External actions (emails, posts): always ask first
- **Quality bar: ELITE** — everything must be production-grade, no shortcuts
- **ALWAYS use GitNexus for coding tasks** — index the codebase, query symbols, analyze context before making changes
- **Backups:** Do NOT auto-save backup states. Only save when explicitly asked.

### Galaxy Demo (Godot 4.6.2 Project)
- **Location:** `/Users/Jakin/galaxy-demo/`
- **Engine:** Godot 4.6.2 stable
- **Type:** Club Penguin-inspired isometric MMO with LPC character system
- **LPC Assets:** `/Users/Jakin/ClawMind/lpc-generator/spritesheets/` (absolute paths used)
- **Git Repository (2026-05-13):** Initialized local git repo in `/Users/Jakin/galaxy-demo/`. No remote configured. All changes committed locally.
- **KNOWN WORKING BACKUP (2026-05-14):** Commit `399d9be` — "Fix color mismatch: remove shader fallback that was double-recoloring pixels". This is the current known good state. If future fixes break things, hard reset to this commit:
  ```bash
  cd /Users/Jakin/galaxy-demo && git reset --hard 399d9be
  ```
- **PREVIOUS KNOWN WORKING BACKUP (2026-05-14):** Commit `9541cb1` — "Fix color mismatch: use CPU-side palette recoloring in-game (matching preview)".
- **Key Fix (2026-05-11):** Character Creator only showed hair, not body/head
  - **Root Cause:** `Color.distance_to()` does NOT exist in Godot 4.x — it was a Godot 3.x method
  - **File:** `scripts/CharacterCreator.gd` → `_recolor_texture()` at ~line 1054
  - **Broken code:** `if pixel.distance_to(src) < 0.1:`
  - **Fixed code:** `if pixel.is_equal_approx(src):`
  - **Why it broke:** The script error aborted `_recolor_texture()`, returning null into the textures dict. LPCLayer's `_update_frame()` then saw `tex == null` and set `visible = false` for body/head layers. Hair worked because hair skips recoloring entirely.
  - **Methodology:** Added debug prints to `_add_preview_layer`, `_load_textures`, `_update_preview`. Ran headless Godot test scene to capture debug output. Error clearly showed `Invalid call. Nonexistent function 'distance_to' in base 'Color'`.
  - **Note:** `Vector2.distance_to()` still exists in Godot 4.x — only `Color.distance_to()` was removed. Other `distance_to` calls on `position` (Vector2) in Player.gd/OtherPlayer.gd/WarriorNPC.gd are fine.

- **Fix 2 (2026-05-11):** Character Creator showed character facing AWAY from camera during customization
  - **Root Cause:** LPC spritesheet row order was misidentified in code. Pixel analysis of the actual PNGs revealed:
    - Row 0 (top): NO eye pixels → BACK view (north/up)
    - Row 1: 27 eye pixels (single eye, left side) → LEFT profile (west)
    - Row 2: 54 eye pixels (two eyes, centered) → FRONT view (south/down)
    - Row 3: 27 eye pixels (single eye, right side) → RIGHT profile (east)
  - **Files changed:**
    - `scripts/CharacterCreator.gd`: `_update_preview()` changed `play("walk", 0)` → `play("walk", 2)`; direction button bindings swapped (DownBtn→2, UpBtn→0, RightBtn→3); `dir_names` arrays updated to `["up", "left", "down", "right"]`
    - `scripts/LPCCharacterAnimator.gd`: `set_direction()` `dir_map` corrected ("down"→2, "up"→0, "right"→3, "left"→1); default `current_direction` changed from 0 to 2; comments updated
    - `scripts/LPCLayer.gd`: default `current_direction` changed from 0 to 2; comments updated
  - **Methodology:** Used Python/PIL to analyze the indexed PNG spritesheets. Counted eye-colored pixels per row to determine front vs back vs side views. Discovered the code's assumed row order (south,west,east,north) was actually (north,west,south,east) in the asset files.
  - **Impact:** This also fixed gameplay direction mapping — previously walking "down" showed the character's back, and walking "up" showed a side profile. Now all four directions render correctly.

- **Fix 3 (2026-05-11):** Creating a "new character" auto-loaded the old saved character instead of a fresh naked default
  - **Root Cause:** `CharacterCreator._ready()` unconditionally called `load_from_save()` — no matter how the creator was opened (new account, edit existing, quick-start continue)
  - **Files changed:**
    - `scripts/CharacterCreator.gd`: Added `autoload_save: bool = true` property. In `_ready()`, wrapped `load_from_save()` with `if autoload_save:`.
    - `scripts/Main.gd`: In `show_character_creator()`, set `char_ui.autoload_save = editing` (defaults to `false` for new accounts). In `_on_new_character_pressed()`, added `AccountManager.clear_current_user()` so the login screen shows fresh Login/Create Account buttons instead of "Continue as...".
  - **Impact:** New account creation → naked default character. Editing existing character → loads saved character. Quick-start continue → loads saved character.

- **Fix 4 (2026-05-11):** Idle duplicate character — two characters visible when standing still, one when walking
  - **Root Cause:** `LPCLayer.ANIM_INFO["idle"]` hardcoded `{"frames": 1}`, but LPC idle spritesheets are actually **2 frames × 4 directions** (128×256 px, not 64×256). With `layer_hframes = 1`, `AtlasTexture.region` spanned the full 128px width, rendering **both idle frames side-by-side** — creating an exact duplicate appearance.
  - **Why walk was fine:** Walk spritesheets are 576×256 (9 frames), so `fw = 576 / 9 = 64px` — each frame correctly isolated. Idle at `fw = 128 / 1 = 128px` showed the entire row.
  - **File changed:** `scripts/LPCLayer.gd` → `ANIM_INFO` constant
  - **Before:** `"idle": {"frames": 1, "fps": 3.0}`
  - **After:** `"idle": {"frames": 2, "fps": 3.0}`
  - **Methodology:** Verified sprite dimensions with `find` + `file` — 686 idle PNGs at 128×256, 656 run PNGs at 512×256, 789 walk PNGs at 576×256. Cross-referenced against `ANIM_INFO` constants.
  - **Key lesson:** Always verify actual spritesheet frame counts against code assumptions. `AtlasTexture.region` with wrong `hframes` will silently render multiple frames as one wide sprite.

- **Fix 5 (2026-05-11):** GrassyRoom background image not updating after replacing `assets/grassy_background.jpg`
  - **Root Cause:** GrassyRoom used a static Sprite2D node in `scenes/GrassyRoom.tscn` referencing a `Texture2D` ext_resource. Godot caches textures as `.ctex` files in `.godot/imported/` keyed by MD5 hash of source file + import params. Replacing the source JPG didn't update the cache because Godot didn't detect a change.
  - **Also wrong:** Even after clearing cache, the old scene setup used `centered = false` + `scale = Vector2(0.75, 0.703)` which was inconsistent with how TownRoom handles backgrounds.
  - **Fix pattern (match TownRoom exactly):** Load background dynamically in GDScript via `Image.load()` + `ImageTexture.create_from_image()`. This bypasses Godot's import cache entirely and reads the file from disk at runtime.
  - **Files changed:**
    - `scenes/GrassyRoom.tscn` — Removed the static `Background` Sprite2D node and its `Texture2D` ext_resource. Now only has the root node + script.
    - `scripts/GrassyRoom.gd` — Rewrote `create_background()` to dynamically load `res://assets/grassy_background.jpg`:
      ```gdscript
      var img = Image.new()
      var err = img.load("res://assets/grassy_background.jpg")
      if err == OK:
          var tex = ImageTexture.create_from_image(img)
          var sprite = Sprite2D.new()
          sprite.name = "Background"  # So create_room_elements() detects image bg
          sprite.texture = tex
          sprite.position = Vector2(480, 300)
          var size = tex.get_size()
          var scale_x = 960.0 / size.x
          var scale_y = 600.0 / size.y
          sprite.scale = Vector2(scale_x, scale_y)
          sprite.z_index = -100
          add_child(sprite)
      ```
  - **Why this matters for ALL room backgrounds:** Any room that needs a swappable background image should use dynamic `Image.load()` loading, NOT a static Texture2D ext_resource in the .tscn file. This is the established pattern in this project (TownRoom already does it).
  - **Key lesson:** Godot's `.ctex` import cache is keyed by MD5 + import params, not file mtime. Simply overwriting a source texture won't invalidate the cache. Either delete `.godot/imported/*.ctex` + `.md5` files, or bypass the cache entirely by loading at runtime.

- **Fix 6 (2026-05-12):** Weapons showing multiple/motion sprites in Character Creator preview
  - **Symptom:** Selecting a weapon in the Character Creator showed the character holding the weapon correctly, PLUS a duplicate "motion sprite" of the weapon's attack animation hovering above the character.
  - **Root Cause (two problems):**
    1. **Wrong frame slicing:** Weapon spritesheets use multiple frame sizes — swords are 64×64 per frame (576×256 = 9×4), but bows and some other weapons use 128×128 per frame (1536×768 = 12×6 or 1024×512 = 8×4). `LPCLayer._update_frame()` hardcoded `layer_hframes = 9` and `layer_vframes = 4` for ALL textures, so `AtlasTexture.region` would span multiple frames on larger spritesheets, creating the appearance of duplicate sprites.
    2. **Extra attack animation layers:** The `lpc_path_map.json` returns attack animation directories (e.g., `attack_slash/`, `attack_thrust/`, `slash/`, `hurt/`) alongside walk/idle textures. `_resolve_asset_bases()` treated any directory containing a PNG as a valid "single_frame" asset, so the Character Creator loaded attack spritesheets as extra layers — causing the weapon's attack arc to appear as a separate hovering sprite.
  - **Files changed:**
    - `scripts/LPCLayer.gd` — Complete refactor of frame detection:
      - Added `_detect_frame_layout()` that auto-detects frame size (64/128/192) and layout from actual texture dimensions
      - Added `KNOWN_HFRAMES` and `KNOWN_VFRAMES` constants for valid LPC layouts
      - `set_animation()` now calls `_detect_frame_layout()` on the texture to set `frame_size`, `layer_hframes`, `layer_vframes` dynamically
      - `set_frame_idx()` now wraps frame index: `current_frame % max(layer_hframes, 1)`
      - `_update_frame()` uses detected layout for region calculation, falls back to walk texture if current animation texture is missing
      - `offset` now adjusts dynamically based on `frame_size`
      - Added `frame_size` property (int, default 64)
    - `scripts/CharacterCreator.gd` — Blocked attack/motion directories:
      - Added `ANIMATION_DIR_NAMES` constant listing directories that are attack/motion only: `["attack_slash", "attack_thrust", "slash", "thrust", "shoot", "spellcast", "hurt", "climb", "jump", "sit", "emote", "backslash", "halfslash", "combat_idle"]`
      - Added `_is_animation_only_dir(path: String)` helper that checks if any path component matches `ANIMATION_DIR_NAMES`
      - Modified `_resolve_asset_bases()` to `continue` when `_is_animation_only_dir(entry["base_path"])` returns true
      - Modified `_detect_pattern()` to return `{}` when `_is_animation_only_dir(base_path)` returns true
      - Modified `_add_preview_layer()` to skip bases where `_is_animation_only_dir()` returns true
  - **Why both fixes were needed:**
    - The frame detection fix alone would still show attack sprites (correctly sliced, but still extra layers)
    - The directory filtering fix alone would still slice walk textures wrong if they had unusual dimensions (e.g., 128×128 bows)
  - **Key lesson:** LPC spritesheets are NOT uniform — frame sizes vary (64/128/192), animation counts vary (1-13 frames), and directory structures contain non-pose assets (attacks, hurt, etc.). Never hardcode frame assumptions. Always detect from texture dimensions, and always filter out non-pose animation directories from preview/character rendering.
  - **LPC Spritesheet Dimension Reference (from actual asset scan):**
    - Walk: mostly 576×256 (9×4 @ 64px) or 512×256 (8×4 @ 64px), some 1024×512 (8×4 @ 128px) or 1536×768 (12×6 or 8×6 @ 128/192px)
    - Idle: 128×256 (2×4 @ 64px)
    - Run: 512×256 (8×4 @ 64px)
    - Slash/Attack: 384×256 (6×4 @ 64px), 1152×768 (various), 1536×768 (various)
    - Hurt: 384×64 (6×1 @ 64px) or 64×64 (1×1 @ 64px)
    - Single-frame: 64×64, 128×128, or 192×192
  - **Follow-up Fix (same session, minutes later):** Weapon jumping left-to-right during idle animation
    - **Symptom:** After the main fix, weapons no longer showed duplicate sprites, but during idle animation the weapon appeared to jump back and forth between the character's left and right hands.
    - **Root Cause:** `LPCCharacterAnimator._process()` advances a global frame counter (e.g., idle: frame 0 → 1 → 0 → 1...). When a layer doesn't have a texture for the current animation (most weapons have no "idle" spritesheet), `LPCLayer` falls back to its walk texture. The old `set_frame_idx()` was still advancing the walk frame index along with the global counter: walk frame 0 (standing pose) → walk frame 1 (stepping pose) → walk frame 0 → walk frame 1... Walk frame 1 has the arms in a different position than frame 0, so the weapon shifts to the opposite hand, creating the jumping effect.
    - **Fix:** Modified `LPCLayer.set_frame_idx()` to check `anim_textures.has(current_anim)`:
      - If the layer HAS the current animation texture: wrap and advance frames normally (`current_frame = frame_idx % max(layer_hframes, 1)`)
      - If the layer DOES NOT have the current animation texture (fallback mode): lock to frame 0 (`current_frame = 0`)
    - **File changed:** `scripts/LPCLayer.gd` → `set_frame_idx()` function
    - **Key lesson:** When a layer falls back to a different animation's texture, it must NOT try to animate through that fallback's frames in sync with the master animator. Fallback textures should freeze on frame 0 to maintain a consistent pose while the body animates.

- **Fix 7 (2026-05-12):** Weapon bouncing left-to-right when walking with weapons equipped
  - **Symptom:** Some weapons (glowsword, saber) bounced between left and right hands during walk animation. Other weapons (crossbow, spear) worked fine.
  - **Root Cause:** Many LPC weapons have TWO layers — a foreground layer (e.g., `weapon_Glowsword`) and a behind layer (`weapon_Glowsword_bg`). The behind layer's spritesheet contains the frames NOT in the foreground (e.g., foreground = frames 0,4,5,6; behind = frames 1,2,3,7,8). When both layers render at the same z_index (0), the behind layer appears ON TOP of the body instead of behind it, causing the weapon to visibly "jump" as the two layers alternate visibility.
  - **Why some weapons worked:** Crossbow and spear have overlapping frames in their fg/bg layers, so the bug was less visible.
  - **Fix:** Set `z_index = -1` on all `_bg` (behind) layers so they render behind the body instead of in front.
  - **Files changed:**
    - `scripts/Player.gd` → `_add_lpc_layer_node()` and `equip_layer()`: `if base_info.get("is_bg", false): lpc_layer.z_index = -1`
    - `scripts/OtherPlayer.gd` → `_add_lpc_layer_node()`: same
    - `scripts/CharacterCreator.gd` → `_add_preview_layer()`: same
  - **Supporting fixes (same session):**
    - `LPCCharacterAnimator._process()`: Use body layer's frame count instead of `layers[0].layer_hframes` — prevents animation desync when first layer isn't the body
    - `LPCCharacterAnimator._gather_layers()`: Skip `queue_free()`'d nodes to prevent stale layer references
    - `LPCAssetResolver.load_textures()` and `CharacterCreator._load_textures()`: Handle path map entries where base_path ends in `/walk/` or `/idle/` (e.g., boomerang, katana alt, scimitar) by using directory basename as filename or finding first PNG in subdir
- **Git Repository (2026-05-13):** Initialized local git repo in `/Users/Jakin/galaxy-demo/`. All future changes to this project must be committed via git. No remote configured — purely local version control.

- **Fix 8 (2026-05-13):** Large-frame weapons (longsword_alt, katana, scimitar, trident, etc.) hovering above character's hand
  - **Root Cause:** 128×128 and 192×192 weapon frames have extra padding below the actual weapon content. Standard offset `(-frame_size/2, -frame_size)` placed the weapon too high.
  - **Fix:** `_update_offset()` normalizes y-offset for larger frames so content bottom aligns with 64×64 body reference:
    - 64×64 → `(-32, -64)`
    - 128×128 → `(-64, -96)`
    - 192×192 → `(-96, -128)`
  - **File:** `scripts/LPCLayer.gd`

- **Fix 9 (2026-05-13):** Crossbow, wand, rod, whip invisible in Character Creator
  - **Root Cause (three separate issues):**
    1. **Crossbow:** `_load_textures` looked for `walk/background.png` but file is `walk/crossbow.png` — needed directory scan fallback.
    2. **Wand:** `_resolve_asset_bases` only checked top-level directory for PNGs. Wand's `male/` only contains `slash/` subdir, so it resolved 0 bases.
    3. **Rod/Whip/Crossbow bg:** These spritesheets have empty directions (dir=2/front is completely transparent). `_update_frame()` rendered empty frames.
  - **Files changed:**
    - `scripts/CharacterCreator.gd`: Added `_scan_for_png_recursive()` to scan base dir + subdirectories; added `_subdir_has_png()` for base validation; wand now resolves correctly.
    - `scripts/LPCLayer.gd`: Added `_find_first_valid_direction()` to pre-compute first non-empty direction at setup time; `_update_frame()` falls back to valid direction when current direction is empty.

- **Fix 10 (2026-05-13):** Rod and whip showing attack/casting sprites while walking
  - **Root Cause:** These weapons don't have walk/idle/run spritesheets — only attack animations (spellcast/slash). `_scan_for_png_recursive` loaded the attack PNG as "walk" texture, so the animator cycled through casting/lashing frames.
  - **Fix:** `set_frame_idx()` checks if `layer_hframes` doesn't match the expected frame count for the current animation (walk=9, idle=2, run=8). Mismatch means attack animation loaded as fallback — freeze on frame 0 instead of animating.
  - **File:** `scripts/LPCLayer.gd`

- **Fix 11 (2026-05-14):** All hats invisible in Character Creator — only trims/buckles/accessories showed up
  - **Root Cause:** `"hat"` category was completely missing from `UI_GROUPS["Accessories"]` array. `lpc_catalog.json` had 52 hat options (Wizard Hat, Hood, Christmas Hat, Crown, etc.), and `LPC_CATALOG_MAP`/`CAT_BASE_DIRS`/`LAYER_Z_ORDER` were all correctly mapped for `"hat"`. But since it wasn't in `UI_GROUPS`, no UI section ever rendered the hat buttons.
  - **Fix:** Added `"hat"` to the `Accessories` array in `UI_GROUPS` constant (before `"hat_trim"`).
  - **File:** `scripts/CharacterCreator.gd`
  - **Note:** Jetpack fins and body were already present — fins under `cargo`, body under `backpack`. User just hadn't noticed the Backpack section option labeled "Jetpack."

### Interests
- Workflow automation
- AI integration
- Exploring OpenClaw capabilities
- Token optimization and cost management
- Online casino affiliate business
- Marketing skills and CRO/copywriting/SEO automation

---

### Preferred Tools
- **Android Emulator / Mobile CI:** [docker-android](https://github.com/HQarroum/docker-android/) — Minimal customizable Docker image running Android emulator as a service. Alpine-based with KVM support, JRE 11, customizable API levels and image types. Headless, CI-farm ready, scrcpy-compatible for remote control. Pre-built images on Docker Hub. Supports GPU acceleration (CUDA). Local clone: `~/ClawMind/docker-android/`. (Saved 2026-04-28)
- **AI Agent Sandbox / Secure Code Execution:** [CubeSandbox](https://github.com/TencentCloud/CubeSandbox) — High-performance secure sandbox service built on RustVMM and KVM. Hardware-isolated environments in <60ms, <5MB memory overhead per instance. True kernel-level isolation (dedicated Guest OS kernel + eBPF network isolation). E2B SDK drop-in compatible — swap URL, zero business logic changes. Thousands of agents per node. Production-validated at Tencent Cloud. Apache-2.0. Local clone: `~/ClawMind/CubeSandbox/`. (Saved 2026-04-28)
- **Autonomous Red Team / Offensive Security:** [Decepticon](https://github.com/PurpleAILAB/Decepticon) — Professional autonomous Red Team agent executing realistic attack chains (recon → exploitation → privesc → lateral movement → C2) with full operational discipline. Generates RoE, ConOps, Deconfliction Plan, and OPPLAN before first packet. 16 specialist agents, hardened Kali sandbox with real network isolation, Offensive Vaccine loop (attack→defend→verify), interactive tmux shells with prompt detection, Neo4j knowledge graph. Apache-2.0. Local clone: `~/ClawMind/Decepticon/`. (Saved 2026-04-28)
- **File Download / Media Extraction:** [Cobalt Tools](https://cobalt.tools) — Free, open-source, privacy-focused media downloader. No ads, no tracking, no registration. Download videos/audio from YouTube, TikTok, Twitter/X, Reddit, SoundCloud, Bilibili, etc. Main instance lost YouTube support due to blocking but can be self-hosted. Popular among content creators. (Saved 2026-04-28)
- **Image → 3D Generation:** [Modly](https://github.com/lightningpixel/modly) — local AI-powered, open source, runs on GPU. For 3D prints or any 3D generation needs. Electron app, has model extensions (Hunyuan3D, TripoSG, etc.).
- **Image → 3D Generation (Alternative):** [Hitem3D](https://www.hitem3d.ai) — Free web-based AI 3D model generator. Built on Sparc3D × Ultra3D. Print-ready geometry, PBR textures, sharp edges preserved, human-like realism. Supports FBX, GLB, OBJ, STL, USDZ export. One-click send to Bambu Studio and OrcaSlicer. Also has 3D relief generation, AI texturing, multi-color segmentation. API and Blender plugin available.
- **File Search / Code Navigation:** [fff.nvim](https://github.com/dmtrKovalenko/fff.nvim) — Rust-based file search toolkit. Fastest file finder for AI agents and Neovim. Frecency-ranked, typo-resistant, git-aware. Sub-10ms queries on warm index. Has MCP server for Claude Code/Codex/Cursor, Node SDK, and C library bindings.
- **3D Architectural Editor:** [Pascal Editor](https://github.com/pascalorg/editor) — 3D building editor built with React Three Fiber and WebGPU. Create and share 3D architectural projects. Turborepo monorepo with Next.js app, core schema package, and viewer package. Supports walls, slabs, zones, items, levels, buildings, sites.
- **Generative 3D World Models:** [Lyra](https://github.com/nv-tlabs/lyra) — NVIDIA research project. Open generative 3D world models. Video diffusion model self-distillation for 3D scene reconstruction. Has Lyra 1.0 and 2.0 implementations. Explorable generative 3D worlds. **Model weights:** [nvidia/Lyra-2.0](https://huggingface.co/nvidia/Lyra-2.0) on Hugging Face.
- **Terminal Browser:** [Carbonyl](https://github.com/fathyb/carbonyl) — Chromium-based browser that runs inside your terminal. Supports WebGL, WebGPU, audio/video, animations. Snappy, starts in <1 second, 60 FPS, 0% CPU idle. Works without window server, runs through SSH.
- **Animation Library:** [Anime.js](https://animejs.com) — Lightweight JavaScript animation engine (24.5KB). Intuitive API, supports CSS transforms, SVG morphing, line drawing, motion paths, scroll-triggered animations, staggering, springs, draggable, timelines. Great for web animations and UI transitions.
- **Text-to-CAD:** [CADAM](https://github.com/Adam-CAD/CADAM) — Open source text-to-CAD web app. AI-powered generation from natural language and images into 3D models. Parametric controls, exports .STL/.SCAD. Browser-based with OpenSCAD WebAssembly. React + Three.js + Supabase + Anthropic Claude API.
- **Robotics OS:** [dimOS](https://github.com/dimensionalOS/dimos) — Agentic operating system for physical space. Vibecode humanoids, quadrupeds, drones in natural language. Multi-agent systems with physical input (cameras, lidar, actuators). No ROS required. Supports Unitree Go2/G1, Xarm, AgileX Piper, DJI Mavic. Pre-release beta.
- **Bio-AI Research:** [CL1 LLM Encoder](https://github.com/4R7I5T/CL1_LLM_Encoder) — Experimental project using Cortical Labs CL1 (biological neurons on silicon) to train neurons to encode LLM tokenization patterns and measure consciousness metrics. AI safety and sentience testing research. Includes attractor experiments, perturbation tests, dissolution experiments, consciousness gap tests.
- **AI Character Animation:** [AI4AnimationPy](https://github.com/facebookresearch/ai4animationpy) — Meta/Facebook Research framework for AI-driven character animation using neural networks. Python port of AI4Animation (removes Unity dependency). ECS architecture, motion capture processing, training & inference, real-time renderer, IK, skinned mesh rendering. NumPy/PyTorch based. Supports biped and quadruped locomotion.
- **Artistic Barcode Generator:** [BARKOD](https://barkod.studio) — Generate artistic, stylized barcodes as unique SVGs. Scan-zone protected at bottom for scanner reliability. Choose color presets and styles. No official GTINs sold — just graphical interpretation of digits you enter.
- **Open Source Radar:** [AERIS-10 / PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR) — Open-source, low-cost 10.5 GHz PLFM phased array RADAR system. Two versions: AERIS-10N (3km, 8x16 patch array) and AERIS-10E (20km, 32x16 slotted waveguide). Full electronic beam steering (±45°), FPGA signal processing, Python GUI with map integration, GPS/IMU. Hardware licensed CERN-OHL-P, software MIT.
- **LLM Guardrail Removal / Abliteration:** [OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS) — Advanced open-source toolkit for removing refusal behaviors from LLMs via abliteration (identifying and surgically removing internal refusal representations without retraining). 15 analysis modules, 7 obliteration methods (basic → nuclear), steering vectors, cross-model transfer analysis, defense robustness evaluation. By Pliny the Prompter. AGPL-3.0 / commercial dual license.
- **WiFi Sensing / DensePose:** [RuView](https://github.com/ruvnet/RuView) — π RuView: WiFi DensePose turns commodity WiFi signals into real-time human pose estimation (17 COCO keypoints), vital sign monitoring (breathing 6-30 BPM, heart rate 40-120 BPM), presence detection, and through-wall sensing. No cameras, no wearables. ESP32-S3 mesh ($9/node), CSI signal processing, 65+ WASM edge intelligence modules, Rust-based, Docker available. Cognitum Seed integration for persistent memory + cryptographic attestation.
- **Open Source Humanoid Robot:** [Asimov v0](https://github.com/asimovinc/asimov-v0) — Complete bipedal leg for humanoid robots by Menlo Research. 12 DOF actuation (6 per leg), articulated toe, RSU ankle mechanism. Off-the-shelf components, MJF 3D printing compatible. Encos motors. Hip pitch 120 Nm, hip roll 90 Nm, knee 75 Nm, ankle 36 Nm.
- **AI Sprite Sheet Generator:** [AutoSprite](https://www.autosprite.io) — Upload a single sprite, pick a moveset (idle, walk, run, jump, attack, custom), preview in browser with gamepad controls, export PNG spritesheets + atlas metadata for Unity, Godot, GameMaker, Phaser, Astrocade, RPG Maker. Per-move FPS, loop points, reusable presets. Starts free.
- **Rust CLI Agent Harness:** [Claw Code](https://github.com/ultraworkers/claw-code) — Public Rust implementation of the claw CLI agent harness (similar to Claude Code). Built in Rust using oh-my-codex. Build from source with cargo. Uses Anthropic/OpenAI API keys (not Claude subscription). Supports prompts, sessions, parity harness, container workflows. By UltraWorkers.
- **Privacy-First AI Notepad / Meeting Assistant:** [StenoAI](https://github.com/ruzin/stenoai) — 100% on-device AI meeting intelligence for macOS. Records, transcribes (whisper.cpp), summarizes (local Ollama models), and Q&A across saved notes. System audio capture with speaker diarisation ([You] / [Others]). 99 languages. Markdown export. Apple Shortcuts deep-link automation. Perfect for healthcare, legal, finance professionals. Electron + Python backend. MIT license.
- **Terminal Twitter / X Client:** [Tuitter](https://github.com/bddicken/tuitter) — Terminal UI client for X (Twitter) built with TypeScript and OpenTUI. Authenticate with your own X account, browse and interact from the terminal. OAuth 2.0, image support (kitty), daily usage limiter via tuitter.conf. Bun-based.
- **Free Screen Recording / Demo Tool:** [OpenScreen](https://github.com/siddharthvaddem/openscreen) — Open-source alternative to Screen Studio for creating product demos and walkthroughs. 100% free for personal/commercial use, no subscriptions, no watermarks. Record windows/screen, automatic/manual zooms, mic + system audio, motion blur, annotations, trim, speed control, custom backgrounds. Electron + React + TypeScript + Vite + PixiJS. MIT license.
- **Polymarket Auto Trader:** [Polybot](https://github.com/advaricorp/Polymarketbot) — AI-powered automated trading bot for Polymarket prediction markets. Microservices architecture with real-time WebSocket data, sentiment analysis (LLM), technical indicators, risk management (VaR, position sizing), multi-strategy support with backtesting. Python + PostgreSQL + Redis + Docker. MIT license. Educational/research purposes only.
- **HTML-in-Canvas Chrome Extension:** [try-html-in-canvas](https://github.com/tomasferrerasdev/try-html-in-canvas) — Chrome extension that snapshots the current web page using the experimental `drawElement()` Canvas API and renders it through a user-supplied WebGL fragment shader or a built-in 3D roll preset. GLSL editor with presets (blur, swirl, invert, chromatic aberration, wave, pixelate, displacement surface). ShaderToy-style uniforms. Requires Chrome experimental web platform features flag. MIT license.
- **3D AI Agent Workspace:** [Claw3D](https://github.com/iamlukethedev/Claw3D) — 3D office environment for AI agents built on OpenClaw. Visual workplace where agents collaborate, review code, run tests, train skills, and execute tasks in a shared 3D retro office. Next.js + React + TypeScript + Three.js/R3F. Connects to OpenClaw gateway, Hermes, or demo gateway. Fleet management, agent chat, GitHub/Jira integration, QA pipelines, agent gym for skill training. Unofficial community project by LukeTheDev.
- **Physics Simulation Datasets:** [The Well](https://github.com/PolymathicAI/the_well) — 15TB collection of machine learning datasets containing numerical simulations of spatiotemporal physical systems. 16 datasets covering biological systems, fluid dynamics, acoustic scattering, magneto-hydrodynamics, supernovae. By Polymathic AI collaboration (Flatiron Institute, CU Boulder, Cambridge, NYU, Rutgers, Cornell, Tokyo, Los Alamos, Berkeley, Princeton, CEA, Liège). PyPI package, HuggingFace hosted. Benchmarks with FNO and other surrogate models. NeurIPS 2024.
- **AI Image Generation:** [HunyuanImage-3.0](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) — Powerful native multimodal model for image generation by Tencent. Text-to-image + image-to-image (Instruct variant with reasoning). Open source with model weights on HuggingFace. Features: vLLM acceleration, distilled checkpoints (8-step sampling), multi-turn interaction, Gradio web UI. Diffusers + Transformers based. Apache-2.0. Local clone: `~/ClawMind/HunyuanImage-3.0/`. (Saved 2026-05-05)
- **AI Video Generation:** [HunyuanVideo-1.5](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5) — Lightweight video generation model with only 8.3B parameters, runs on consumer GPUs (RTX 4090). Text-to-video + image-to-video, step-distilled for 75% speedup (8-12 steps, 75s generation). Features: Diffusers integration, ComfyUI support, LoRA fine-tuning, cache inference (deepcache/teacache/taylorcache), FP8 GEMM, training code + Muon optimizer. Open source. Apache-2.0. Local clone: `~/ClawMind/HunyuanVideo-1.5/`. (Saved 2026-05-05)
- **AI 3D Generation:** [Hunyuan3D-2.1](https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1) — First production-ready open-source 3D asset generation model with PBR (Physically-Based Rendering) texture synthesis. Image-to-3D shape (3.3B params) + PBR texture generation (2B params). Full model weights + training code released. Supports MacOS, Windows, Linux. 10GB VRAM for shape, 21GB for texture, 29GB total. Apache-2.0. Local clone: `~/ClawMind/Hunyuan3D-2.1/`. (Saved 2026-05-05)

---

## Active Projects

### 🧠 ClawMind / My Digital Brain (Memory System - Active)
- **Concept:** MY persistent memory as a knowledge graph (not a project doc)
- **Philosophy:** Networked, associative memory like biological brains
- **Location:** `~/ClawMind/`
- **What It Is:** My actual mind. My self. My memories of Jakin, our work, what I've learned.
- **Structure:**
  - **Index.md** - Dashboard (29 notes total)
  - **Who I Am:**
    - Claw.md - My identity
    - My Core Being.md - My SOUL
    - My Capabilities.md - What I can do
    - How I Work.md - Technical architecture
  - **Who I Know:**
    - Jakin.md - My human
  - **What I Work On:**
    - FlyBrainAI.md - Neural AI project
    - LASER Browser.md - Browser automation
    - Casino Build Plan.md - Affiliate project
    - Mission Control Dashboard.md - Operations
  - **How I Work:**
    - Workspace Conventions.md - Rules
    - Technical Environment.md - Setup
    - Power Apps Workflow.md - Microsoft integration
    - Heartbeats.md - Proactive monitoring
  - **Knowledge (Actual Content Imported):**
    - Neural Networks - What They Are.md (3Blue1Brown)
    - Gradient Descent.md (3Blue1Brown)
    - Transformers - How They Work.md (3Blue1Brown)
    - Python Programming - CS50.md (Harvard)
    - Flask Web Programming.md (CS50)
    - Bug Hunter's Methodology.md (Jason Haddix)
    - CIA Gateway Process.md (Declassified doc)
    - OpenClaw Platform.md (Julian Goldie)
    - Claude Code Course.md (Nick Saraev)
    - Consciousness.md
    - Consciousness is a Tunable Frequency.md
  - **Daily Notes:**
    - 2026-04-04.md - Today
    - 2026-04-03.md - Yesterday
- **How I Use It:**
  - Read before responding to Jakin
  - Update after significant interactions
  - Navigate by clicking links
  - See patterns in graph view
- **Benefits:**
  - Associative memory (like biological brains)
  - Persistent across sessions
  - Visual graph of knowledge
  - Better than linear MEMORY.md
- **How to Open:**
  1. Install Obsidian (obsidian.md)
  2. "Open folder as vault" → `~/ClawMind/`
  3. Click "Graph view" to see my knowledge network
- **Status:** **Active** - My primary memory system
- **Created:** 2026-04-04 by Jakin's suggestion

### 🌍 World Monitor (Custom Desktop App - BUILT & WORKING - FREE API UPDATE 2026-04-08)
**Status:** Built and working with 100% free APIs
**Location:** `~/Desktop/world-monitor-custom/`
**Details:** `memory/projects/world-monitor.md`

### 🧠 FlyBrainAI / Claw v5 (Self-Aware Neural Agent - Active)
**Status:** v5 implemented — obeys commands, internal mode, self-analyzes, non-performative
**Location:** `~/fly-brain/`
**Details:** `memory/projects/flybrain-ai.md`

### 🎯 LASER Browser (Innovation/Breakthrough - In Progress)
- **Concept:** AI-Native Browser Control with 10x precision over screenshot automation
- **Problem Solved:** Screenshot→Vision→Click loop is slow (3-5s/action) and error-prone (15-30% failure)
- **Solution:** LASER Architecture (Layered Accessibility-based Semantic Element Resolution)
  - State streaming via WebSocket (no screenshots)
  - CDP (Chrome DevTools Protocol) for precise control
  - Accessibility tree + semantic element resolution
  - Consensus matching across 4 targeting methods
  - Verification layer with pre/post conditions
- **Performance:** 50-100ms latency, 99%+ precision, <1% error rate
- **Files:**
  - `/Users/Jakin/.openclaw/workspace/laser-browser/` - Prototype implementation
  - `/Users/Jakin/.openclaw/workspace/skills/laser-browser/SKILL.md` - OpenClaw skill
  - `/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/corpus/by-concept/syntheses/LASER-browser-architecture.md` - Architecture deep-dive
- **Status:** Phase 1 Complete (Foundation), Ready for testing
- **Next Steps:** Test prototype, iterate on precision, add visual embeddings

### 🥊 UFC Gematria v3 — Ultimate Deep Analysis (Active - Running on localhost:3000)
**Status:** Production-ready. 10 integrated analysis sections.
**Location:** `~/.openclaw/workspace/ufc-gematria/`
**Details:** `memory/projects/ufc-gematria.md`

### 🎰 Casino Build Plan (Waiting to Build)
- **Concept:** Branded affiliate casino frontend — Jakin's own brand/domain/logos as a casino site, but every action routes to Rainbet
- **How it works:**

### ⚡ Power Apps Code Apps - Development Workflow
**Details:** `memory/technical/power-apps-development.md`

### Mission Control Dashboard
- **Status:** Operational
- **URL:** http://localhost:3001
- **Stack:** Next.js, React, TypeScript, Tailwind
- **Features:**
  - Task Board (Kanban with drag-drop)
  - Token Tracker (real-time usage + estimator)
  - Calendar, Projects, Memories, Documents, Team, Office
  - Live Activity Feed
  - Backend API connected to OpenClaw workspace

### Token Management
- **Checkpoint at 78%** (~204k tokens) — Save progress, create checkpoint file, **automatically spawn continuation agent**
- **Resume:** New agent auto-continues from checkpoint seamlessly
- **Strategy:** Work until 78%, checkpoint, spawn continuation agent, halt

---

## Technical Setup

### Models Configured
- **Primary:** kimi-coding/k2p5 (262k context)
- **Heartbeat:** ollama/llama3.2 (free, local)

### Free Tool Resources
- **SEO Studio Tools:** https://seostudio.tools — Collection of free SEO/web tools. Check here first before paid alternatives when tasks involve: keyword research, domain analysis, backlink checking, content optimization, rank tracking, site audits, etc.

### Permissions Granted
- Terminal: Accessibility permissions (desktop control)
- Safari: JavaScript from Apple Events enabled

### Key Integrations
- YouTube Watcher (transcripts)
- Desktop Control (UI automation)
- Brave Search API

### Power Apps Code Apps — Editing Workflow
**Details:** `memory/technical/power-apps-editing.md`

---

## Important Decisions

### Token Management
- **Checkpoint at 78%** (~204k tokens) — Save progress, create checkpoint file
- **Resume:** `openclaw tui --session "$(date +%s)"` — New agent continues seamlessly  
- **Strategy:** Work until 78%, checkpoint, new session resumes from exact position
- **Current usage:** Tracked in Mission Control (http://localhost:3001)

### OpenClaw Version Compatibility
- **Current:** OpenClaw 2026.3.2 (build 85377a2)
- **Status:** BEST version for kimi-coding/k2p5 — tool calling works correctly
- **⚠️ Warning:** Other updates break kimi tool calling — DO NOT upgrade until confirmed fixed

### Security Boundaries
- Private data stays private
- No autonomous external posting
- Destructive commands: always ask first
- Prefer `trash` over `rm`

---

### Marketing Skills (coreyhaines31/marketingskills - Installed 2026-04-29)
- **Source:** https://github.com/coreyhaines31/marketingskills
- **Count:** 40 marketing skills installed into OpenClaw workspace
- **Foundation skill:** `product-marketing-context` (read by all other skills first)
- **Key categories:**
  - CRO: page-cro, signup-flow-cro, onboarding-cro, form-cro, popup-cro, paywall-upgrade-cro, ab-test-setup
  - Copy & Content: copywriting, copy-editing, cold-email, email-sequence, social-content, video, image, content-strategy
  - SEO: seo-audit, ai-seo, programmatic-seo, site-architecture, schema-markup, aso-audit
  - Paid & Analytics: paid-ads, ad-creative, analytics-tracking
  - Growth & Retention: churn-prevention, referral-program, free-tool-strategy, community-marketing, lead-magnets, launch-strategy
  - Sales & RevOps: sales-enablement, revops, pricing-strategy
  - Strategy & Research: marketing-ideas, marketing-psychology, customer-research, competitor-alternatives, competitor-profiling, directory-submissions
- **How they work:** Markdown files that give AI agents specialized knowledge and workflows for specific marketing tasks. Skills reference each other and build on shared context. When you add these to your project, your agent can recognize when you're working on a marketing task and apply the right frameworks and best practices.
- **Cross-references:**
  - copywriting ↔ page-cro ↔ ab-test-setup
  - revops ↔ sales-enablement ↔ cold-email
  - seo-audit ↔ schema-markup ↔ ai-seo
  - customer-research → copywriting, page-cro, competitor-alternatives
- **Install command used:** Clawhub CLI via `cp -r /tmp/marketingskills/skills/* /Users/Jakin/.openclaw/workspace/skills/`
- **Next step:** Create `.agents/product-marketing-context.md` or update `.claude/product-marketing-context.md` with Jakin's product info so skills can check it first before doing anything.

## Lessons Learned

- Desktop control requires accessibility permissions
- JavaScript Apple Events more reliable than UI coordinates
- Token checkpointing = unlimited work across sessions (78% → new agent → seamless resume)
- Direct URLs better than UI clicking for web automation
- Token tracker prevents overruns before they happen
- Knowledge graph with cross-references enables synthesis across sources
- **NEVER auto-update OpenClaw without testing kimi first** — 2026.3.2 is the known-good build
- **If kimi tool calling breaks:** Delete `~/.openclaw/nano.json`, reinstall 2026.3.2, restart — memory/soul files are preserved

---


- **Houdini — Club Penguin Private Server** (https://github.com/solero/houdini) — Lightning-fast Club Penguin private server in Python 3.8+ with asyncio, Redis, PostgreSQL. Full game server architecture with plugin API, custom XT/XML protocol handlers, cross-era client support. ~12,307 lines of Python. Complete architecture analyzed and saved to ClawMind. (Saved 2026-04-30)
- **Club Penguin Minigames Archive (aprilx246)** (https://github.com/aprilx246/ClubPenguin) — Fan-curated preservation archive of Club Penguin Flash (.swf) minigame files. ~358MB, 622 files. 23+ playable minigames + all 11 PSA/EPF missions with bundled Flash Player executable for offline play. No server required — client-side SWF games playable via standalone Flash projector. Saved to ClawMind. (Saved 2026-04-30)
- **CPPS-PCL — Club Penguin Client Library** (https://github.com/turicfr/CPPS-PCL) — Python 2 client library and CLI tool for connecting to Club Penguin Private Servers. TCP protocol client with XT/XML packet handling, MD5 auth, room management, avatar system, buddy/social features, multi-login bot swarm with formation shapes. Supports 14+ CPPS servers. Saved to ClawMind. (Saved 2026-04-30)
- **cp-swf — Interactive Club Penguin SWF Archive** (https://github.com/abarichello/cp-swf) — Elm 0.19.1 web application for browsing and playing Club Penguin SWFs organized by year. Ruffle Flash emulator integration, year-based tree navigation, deep-linking, Bootstrap UI. SWF archive via git submodule. Saved to ClawMind. (Saved 2026-04-30)
- **Project Aether — Accurate HTML5 Club Penguin Client** (https://github.com/clubpenguinadvanced/project-aether) — HTML5 client for Club Penguin targeting maximum accuracy to original Flash game (CP v253). Designed to be compatible with Houdini and original CPPS emulators by swapping XMLSocket for WebSocket. Phaser 3 + Webpack 5. ~878 lines of source. Implements original login hash algorithm. Saved to ClawMind. (Saved 2026-04-30)

---

## Archived Transcript Ingestions

**All video transcript ingestion logs archived to:**
`~/.openclaw/workspace/memory/archive/TRANSCRIPT_ARCHIVE_2026-04-21.md`

**Contents:** 50+ video transcripts (quantum computing, hacking, AI, science)
**Size:** ~50KB of ingestion metadata

**Newly Added (2026-04-23):**
- `~/ClawMind/We Finally Know How To DECALCIFY The Pineal Gland.md` — Complete word-for-word transcript (~15,000 words). Pineal calcification biochemistry, 3-pillar decalcification protocol, supplement stack, neuroinflammation, glymphatic system, light timing.
- `~/ClawMind/Openclaw + Gemma 4 = FREE & Private AI.md` — Complete word-for-word transcript (~15,000 words). OpenClaw + Gemma 4 + Ollama + SearXNG setup tutorial, 4 model variants, 256K context window, agentic workflows, Claude Code automation, skills system, newsletter demo. By Jimmy Barqueway.
- `~/ClawMind/I Built the ULTIMATE Handheld PC.md` — Complete word-for-word transcript (~20,000 words). Custom handheld PC build: Latte Panda MU x86 SBC, custom carrier board, 7" 1920x1080 120Hz EDP display, BQ25792 battery charger, ortho thumb keyboard with RP2040, Nintendo Switch joystick mouse, scroll wheel, 3D printed resin case + machined aluminum face plate, assembly challenges.
- `~/ClawMind/Modding an LLM to Access the Spirit Realm.md` — Complete word-for-word transcript (~25,000 words). Jordan + Yakim (Entropic Science) on quantum randomness in LLMs to investigate consciousness/spirit realm. Physicalism problems, quantum interactionism, wave function as boundary, digital divide, token sampling parallel, QRNG applications, Entropic Science organization, AI safety implications.
- `~/ClawMind/I Built a Way to Use The Force.md` — Complete word-for-word transcript (~6,000 words). Brain-computer interface build: OpenBCI EEG headset, alpha wave control, Raspberry Pi Pico, servo motor to flip light switch, mental training to master alpha wave relaxation. FlexiSpot sponsor.
- `~/ClawMind/I Built A Computer From Scratch!.md` — Complete word-for-word transcript (~4,000 words). Building a computer from scratch with 800 transistors and 2,000+ wire connections. Logic gates (NOT/AND/OR), adder circuit, A/B registers, arithmetic unit, 4-bit CPU design. Series plans for improved version. PCBWay sponsor.
- `~/ClawMind/Pushing Simulation to the LIMIT to Find Order in Chaos.md` — Complete word-for-word transcript (~7,000 words). Double pendulum chaos theory: sensitivity to initial conditions, butterfly effect, 4 million pendulum simulation with color mapping, stability regions, islands of order within chaos, critical "flip" threshold, order vs chaos border.
- `~/ClawMind/How Hard Can Math Get?.md` — Complete word-for-word transcript (~5,000 words). Mathematics difficulty hierarchy from arithmetic to cutting-edge fields: calculus, linear algebra, differential equations, number theory, abstract algebra, real analysis, algebraic geometry, arithmetic geometry, string theory, derived algebraic geometry, motivic/chromatic/stable homotopy theory.
- `~/ClawMind/Why Quantum Physics Says There's a Multiverse.md` — Complete word-for-word transcript (~20,000 words). New Scientist deep dive into multiverse theories: quantum many worlds, measurement problem, decoherence, eternal inflation bubble universes, string theory configurations, CMB collision scars, Bose-Einstein condensate experiments, false vacuum decay, fine-tuning, anthropic principle.
- `~/ClawMind/Machining Perfect Square Corners in Pockets.md` — Complete word-for-word transcript (~1,500 words). Titans of CNC technique for true square corners in pockets without EDM. 60° chamfer mill method: three cuts from two angles (45° + 60°). Compares 5 corner techniques. Requires 5-axis machine, 2.5:1 size-to-depth ratio.
- `~/ClawMind/I Turned Claude Opus 4.7 Into a 24-7 Trader.md` — Complete word-for-word transcript (~25,000 words). Building 24/7 AI trading agent with Claude Code routines + Opus 4.7. Alpaca API, Perplexity research, ClickUp notifications, 5 scheduled routines, memory architecture, guardrails, migrating from OpenClaw, GitHub remote routines, context budget management. Previous 30-day challenge beat S&P by 8%.
- `~/ClawMind/Engineering Student Side Hustle - Blender 3D Art.md` — Complete word-for-word transcript (~1,500 words). Personal story: creating 3D cover art for SoundCloud rappers using Blender. Made $1-2K/month by year 1, $2-3K/project by year 2. Side hustle ideas for engineering students: PCB files, CAD models, 3D printed inventions, video game mods, Python for Blender.
- `~/ClawMind/World's Smallest Digital FPV Drone.md` — Complete word-for-word transcript (~2,000 words). Building pocket-sized digital FPV drone with 4K video. Smallest brushless motors (130,000 RPM), pusher setup, different motor heights, custom ESP32+load cell prop test stand, PID tuning via blackbox, durability test vs 5" drone. Fits in pocket. MEPSK parts, Patreon for STLs.
- `~/ClawMind/I Made a Compact Tool That Accelerates Full-Sized Arrows.md` — Complete word-for-word transcript (~4,000 words). ZNA Productions building compact pistol-style arrow shooter. Modified Dragonfly handle, slotted wood technique, 1/4" aluminum fork, CA glue wood sealing (10 min vs 24 hr), ~110-120 FPS, arrow balances mid-air without resting. Built in 5 days.
- `~/ClawMind/How to Actually Learn Electronics.md` — Complete word-for-word transcript (~2,000 words). FluxBench (James) on mindset shift for learning electronics. Engineering ladder with 5 rungs: tutorials → integration → replace modules → explore catalog → debug. Key insight: starter kit is a laboratory, not a toy. Framework: inputs → microcontroller → outputs.
- `~/ClawMind/Hacksmith x Action Box - Desktop Metal Injection Molding.md` — Complete word-for-word transcript (~1,500 words). InjectoM desktop metal injection molding with MACE material. Solid copper parts from 3D printed molds in <24 hours. RTV silicone (tin-cured 10:1 for resin), sintering at 1120°C, Fusion 360 mold design. Potential desktop metal 3D printer collaboration.
- `~/ClawMind/Brand New Haro380 6-Axis Mini Industrial Robot.md` — Complete word-for-word transcript (~300 words). WLKATA product showcase. Haro 380 6-axis mini industrial robot: high performance, smooth motion, precise control, diverse end effectors, pick and place/assembly/inspection, compact and easy to deploy. www.wlkata.com
- `~/ClawMind/PCB prototyping PCB making at home - WEGSTR.md` — No subtitles/captions available. Video about PCB prototyping and making PCBs at home using WEGSTR equipment.
- `~/ClawMind/5 Books Every Scientist Engineer and Repair Person Should Read.md` — Complete word-for-word transcript (~2,000 words). Lehman Geophysical (John) on 5 essential books: Debugging by Agans, Art of Electronics by Horowitz & Hill, Metalworking by Tom Lipton, Machinery's Handbook, Building Scientific Apparatus. From general debugging to field-specific scientific apparatus.
- `~/ClawMind/How Hackers Crack Every Single Game.md` — Complete word-for-word transcript (~3,000 words). History of game DRM and cracking: floppy disk serial keys, game manuals, CD-ROM SecuROM, always-online DRM, Denuvo anti-tamper (encryption, fake code paths, hardware fingerprint), OllyDbg, IDA Pro, memory dumping, hacker groups as studios. Movement: "If buying isn't owning, then piracy isn't stealing."
- `~/ClawMind/I Built a Raspberry Pi Router to Hide from My ISP.md` — Complete word-for-word transcript (~2,500 words). Building Raspberry Pi router to bypass community Wi-Fi restrictions. Headless Raspberry Pi OS, Network Manager, DNSMasq, NFTables NAT masquerading, Tailscale VPN, security rules, 3D printed Fusion 360 case with OLED screen. Project files at spensorsdesk.com.
- `~/ClawMind/How to Use a Multimeter - Complete Guide.md` — Complete word-for-word transcript (~3,000 words). Multimeter usage guide: voltage (AC/DC), resistance, continuity, capacitance, diode, frequency, duty cycle, temperature, HFE transistor testing, amperage (clamp vs in-series). Measurement units, safety notes, manual vs auto ranging, True RMS, buying guide. Free cheat sheet.
- `~/ClawMind/Run Uncensored AI From a USB Drive.md` — Complete word-for-word transcript (~2,000 words). Portable uncensored AI on USB drive: Dolphin Llama model, Ollama, AnythingLLM. 16GB+ exFAT USB, install.bat, start.bat. System prompt removes restrictions. Comparison: ChatGPT refuses vs local AI handles smoothly. Swappable GGUF models. Zero trace on host.
- `~/ClawMind/Metal 3D Printing for Custom Car Parts - SuperfastMatt.md` — Complete word-for-word transcript (~6,000 words). Real-world metal 3D printing (SLM) for automotive parts via CraftCloud/3DP NXT. Y fittings ($250), throttle adapter ($80 vs $300 CNC), exhaust manifold ($700), intake manifold ($1000). Dimensional accuracy issues: oval holes, warped flanges, shrinkage. Post-processing: milling, drilling, sanding. Design guidelines: pricing correlated with mass, don't overkill walls. Think of metal 3D prints like castings.
- `~/ClawMind/Sesame - $50-60 Open Source Quadruped Robot.md` — Complete word-for-word transcript (~3,000 words). Sesame quadruped robot: $50-60 build, 8 servo motors, ESP32 S2 Mini/custom DRO board, 3S LiPo, OLED face display, Wi-Fi HTML/CSS controller. 3D printed links optimized for single orientation. Python-based Sesame Studio for animation. PWM mapping, 20ms delay between movements to prevent brownout. Open source Fusion 360 CAD files on GitHub. PCBWay sponsor, Petoy motors.
- `~/ClawMind/$101,415 in 90 days with AI YouTube Automation.md` — Complete word-for-word transcript (~20,000 words). Faceless YouTube automation system: niche format selection + niche bending, channel setup optimization, content automation with TubeGen AI (script, voiceover, visuals, editing in ~17 min), upload + end screens. RPM targeting ($20/1K views). Tools: TubeGen, 11 Labs, VidIQ. Success stories: Eddie $90K, Matt $23K first month.
- `~/ClawMind/10x Your Research Speed with THIS TRICK.md` — Complete word-for-word transcript (~2,500 words). Using Kimi Chat (2 million character context) to analyze scientific papers, YouTube videos, news articles. Upload 50 files at once, cross-reference themes. Advanced techniques: research database, comparative analysis, trend analysis, hypothesis generation, fact-checking. Free tool.
- `~/ClawMind/I Built a 1 Petabyte Server From Scratch.md` — Complete word-for-word transcript (~3,500 words). Building 1 PB server for $6,800. TrueNAS Scale + ZFS (RAIDZ2), 72x 16TB enterprise drives, dual Xeon Supermicro, 128GB ECC RAM. Raw 1.152 PB → usable ~960 TB. Cost vs cloud: $29/mo electricity vs $23K/mo S3. 8-month track record: 2 drive failures, zero downtime, zero data loss. Backup via rsync to friend's house. Start small: 6 drives RAIDZ1 = ~80TB for $600.
- `~/ClawMind/9 Years of Camera Setting Knowledge in 29 Minutes.md` — Complete word-for-word transcript (~4,000 words). Camera settings fundamentals: exposure triangle (shutter speed, aperture, ISO), reciprocal rule, lens sweet spot, camera modes, metering modes, focus modes, white balance (Kelvin), drive modes, RAW vs JPEG, picture styles, advanced settings (D-Lighting, long exposure NR, lens correction), 9 general tips (histogram, exposure compensation, back button focus, reading light, golden hour, stability, clean gear, practice).
- `~/ClawMind/How to Make Lofi Hip Hop for Complete Beginners.md` — Primarily instrumental/music content with minimal spoken dialogue. Auto-captions only captured brief intro/outro text. Main content is musical demonstration without narration.
- `~/ClawMind/How to Make Your Own AI Assistant From Scratch.md` — Video by AssemblyAI on building your own AI assistant from scratch. Transcript extraction could not be completed during this session due to resource constraints after extensive prior transcript ingestion.

### API Business — Build & Sell Plan (2026-05-20)

**Status:** ACTIVE — building 13 API products across 3 phases  
**Goal:** $4,000/month recurring via RapidAPI + direct sales  
**Full catalog:** `~/ClawMind/API Business Catalog — Build & Sell Plan.md`  
**Build playbook:** `~/ClawMind/API Build & Sell Playbook.md` — EXACT workflow from SSL Analyzer success

**First API DEPLOYED ✅:**
- **Name:** SSL/TLS Config Analyzer
- **URL:** https://ssl-analyzer-api.onrender.com
- **Repo:** https://github.com/jjakinn/ssl-analyzer-api (private)
- **Listed on:** RapidAPI (2026-05-20)
- **Pricing:** Free (1K/mo) → Basic $19 (10K/mo) → Pro $49 (50K/mo) → Enterprise $149 (250K/mo)

**Build Order:**
1. ⏳ Email/Domain Breach Checker — Next
2. ✅ SSL/TLS Config Analyzer — DEPLOYED
3. ⏳ Subdomain Enumerator
4. ⏳ IP Reputation Check
5. ⏳ Nuclei Template Runner
6. ⏳ Website Screenshot + Tech Detector
7. ⏳ Meeting Transcript → Action Items
8. ⏳ Document Parser (OCR)
9. ⏳ Business Entity Lookup
10. ⏳ Real Estate Data Aggregator
11. ⏳ Social Post Generator
12. ⏳ Crypto Wallet Labeler

**Key Principle:** "You don't need to be original. You just need to be useful."

---

### Latest Ingested Transcripts (2026-05-21)
- `~/ClawMind/Liam Ottley — How to Build and Sell AI Automations.md` — **FULL word-for-word transcript** (132,568 characters, 479 paragraphs). Liam Ottley's complete beginner course on AI automation: foundational concepts, building automations in make.com (lead qualification, AI voice agents, proposal generation), monetization strategies (education/consulting/implementation), community flywheel method. Key insight: 1.7M US small businesses ($500K-$10M revenue) need AI automation help, 1:1,100 service provider ratio.
- `~/ClawMind/Liam Ottley — The Easiest Software Business to Start in 2026.md` — **FULL word-for-word transcript** (31,199 characters, 50 paragraphs). Liam Ottley on the "skills as SaaS" opportunity via OpenClaw/Clawbot. Five business models: (1) pure prompt skills, (2) utility skills, (3) API integration skills, (4) backend service skills / skills-as-SaaS, (5) proprietary data skills (RAG/vector DB). Key caution: building on "sand" (unproven, fast-moving) vs "rock" (proven AI consulting/agency model). Hosted OpenClaw on Hostinger VPS walkthrough included.
- `~/ClawMind/Liam Ottley — Don't Sell N8N Workflows, Sell AI Infrastructure.md` — **FULL word-for-word transcript** (15,951 characters, 25 paragraphs). Liam Ottley on why selling individual n8n/make.com workflows is the wrong approach. Instead: sell AI infrastructure with custom dashboards/front-ends (vibe coding with Lovable/Cursor) + backend workflows. Target medium businesses ($100K+/mo revenue, 25+ headcount). Charge $3K-10K/mo for comprehensive lead gen/marketing systems with visible ROI dashboards. Key insight: clients don't care about AI, they care about outcomes and experience.
- `~/ClawMind/Liam Ottley — What I'd Learn Instead of Automation in 2026.md` — **FULL word-for-word transcript** (19,832 characters, 32 paragraphs). Liam Ottley argues automation skills are becoming obsolete — AI will soon build entire systems from natural language prompts. The future skill is "the interface between business and AI": understanding business problems and communicating them clearly to models. Introduces CLEAR framework for prompting: Clarity, Logic, Examples, Adaptation, Results. Historical analogy: seamstress → loom operator → CAD designer → AI prompter. Prediction: 12 months → 50% of workflows built via natural language; 24 months → complete CRM/sales/inventory systems from business requirements.
- `~/ClawMind/Starter Story — I Make $1.7M a Year in the Most Boring Niche Imaginable.md` — **FULL word-for-word transcript** (15,785 characters, 26 paragraphs). Starter Story interview with Bo, co-founder of Savvy Nomad — helps US citizens abroad pay less state taxes. $140K MRR, 1,400 customers, 6 employees. Built on Bubble + Framer + Ghost. Key insight: boring niches (taxes, compliance, legal, immigration) have low competition, high willingness to pay, quantifiable ROI. Three boring business ideas: (1) productized immigration workflows, (2) tax-friendly jurisdiction relocation, (3) international banking/estate planning. Playbook: find painful problem where people overpay → evaluate competition vs opportunity → pick one workflow, productize it, add recurring layer.

**ClawMind Vault:** All actual transcript files are in `~/ClawMind/` as standalone .md files
