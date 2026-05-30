# Galaxy Demo — Godot Fix Log Archive

**Project:** `/Users/Jakin/galaxy-demo/`  
**Engine:** Godot 4.6.2 stable  
**Type:** Club Penguin-inspired isometric MMO with LPC character system  
**LPC Assets:** `/Users/Jakin/ClawMind/lpc-generator/spritesheets/` (absolute paths used)  
**Known Good Commit:** `399d9be` — "Fix color mismatch: remove shader fallback that was double-recoloring pixels"  
**Previous Good Commit:** `9541cb1` — "Fix color mismatch: use CPU-side palette recoloring in-game (matching preview)"  
**Git:** Local repo initialized 2026-05-13, no remote configured.

---

## Fix 1 (2026-05-11): Character Creator only showed hair, not body/head

**Root Cause:** `Color.distance_to()` does NOT exist in Godot 4.x — it was a Godot 3.x method

**File:** `scripts/CharacterCreator.gd` → `_recolor_texture()` at ~line 1054  
**Broken:** `if pixel.distance_to(src) < 0.1:`  
**Fixed:** `if pixel.is_equal_approx(src):`

**Why it broke:** The script error aborted `_recolor_texture()`, returning null into the textures dict. LPCLayer's `_update_frame()` then saw `tex == null` and set `visible = false` for body/head layers. Hair worked because hair skips recoloring entirely.

**Note:** `Vector2.distance_to()` still exists in Godot 4.x — only `Color.distance_to()` was removed.

---

## Fix 2 (2026-05-11): Character Creator showed character facing AWAY from camera during customization

**Root Cause:** LPC spritesheet row order was misidentified in code. Pixel analysis of the actual PNGs revealed:
- Row 0 (top): NO eye pixels → BACK view (north/up)
- Row 1: 27 eye pixels (single eye, left side) → LEFT profile (west)
- Row 2: 54 eye pixels (two eyes, centered) → FRONT view (south/down)
- Row 3: 27 eye pixels (single eye, right side) → RIGHT profile (east)

**Files changed:**
- `scripts/CharacterCreator.gd`: `_update_preview()` changed `play("walk", 0)` → `play("walk", 2)`; direction button bindings swapped (DownBtn→2, UpBtn→0, RightBtn→3); `dir_names` arrays updated to `["up", "left", "down", "right"]`
- `scripts/LPCCharacterAnimator.gd`: `set_direction()` `dir_map` corrected ("down"→2, "up"→0, "right"→3, "left"→1); default `current_direction` changed from 0 to 2
- `scripts/LPCLayer.gd`: default `current_direction` changed from 0 to 2

**Impact:** This also fixed gameplay direction mapping — previously walking "down" showed the character's back, and walking "up" showed a side profile.

---

## Fix 3 (2026-05-11): Creating a "new character" auto-loaded the old saved character instead of a fresh naked default

**Root Cause:** `CharacterCreator._ready()` unconditionally called `load_from_save()` — no matter how the creator was opened (new account, edit existing, quick-start continue)

**Files changed:**
- `scripts/CharacterCreator.gd`: Added `autoload_save: bool = true` property. In `_ready()`, wrapped `load_from_save()` with `if autoload_save:`.
- `scripts/Main.gd`: In `show_character_creator()`, set `char_ui.autoload_save = editing` (defaults to `false` for new accounts). In `_on_new_character_pressed()`, added `AccountManager.clear_current_user()` so the login screen shows fresh Login/Create Account buttons instead of "Continue as...".

---

## Fix 4 (2026-05-11): Idle duplicate character — two characters visible when standing still, one when walking

**Root Cause:** `LPCLayer.ANIM_INFO["idle"]` hardcoded `{"frames": 1}`, but LPC idle spritesheets are actually **2 frames × 4 directions** (128×256 px, not 64×256). With `layer_hframes = 1`, `AtlasTexture.region` spanned the full 128px width, rendering **both idle frames side-by-side**.

**Fix:** `scripts/LPCLayer.gd` → `ANIM_INFO` constant: `"idle": {"frames": 2, "fps": 3.0}`

**Key lesson:** Always verify actual spritesheet frame counts against code assumptions. `AtlasTexture.region` with wrong `hframes` will silently render multiple frames as one wide sprite.

---

## Fix 5 (2026-05-11): GrassyRoom background image not updating after replacing `assets/grassy_background.jpg`

**Root Cause:** GrassyRoom used a static Sprite2D node in `scenes/GrassyRoom.tscn` referencing a `Texture2D` ext_resource. Godot caches textures as `.ctex` files in `.godot/imported/` keyed by MD5 hash of source file + import params. Replacing the source JPG didn't update the cache.

**Fix pattern (match TownRoom exactly):** Load background dynamically in GDScript via `Image.load()` + `ImageTexture.create_from_image()`. This bypasses Godot's import cache entirely and reads the file from disk at runtime.

**Files changed:**
- `scenes/GrassyRoom.tscn` — Removed the static `Background` Sprite2D node and its `Texture2D` ext_resource.
- `scripts/GrassyRoom.gd` — Rewrote `create_background()` to dynamically load `res://assets/grassy_background.jpg`

**Key lesson:** Godot's `.ctex` import cache is keyed by MD5 + import params, not file mtime. Simply overwriting a source texture won't invalidate the cache. Either delete `.godot/imported/*.ctex` + `.md5` files, or bypass the cache entirely by loading at runtime.

---

## Fix 6 (2026-05-12): Weapons showing multiple/motion sprites in Character Creator preview

**Root Cause (two problems):**
1. **Wrong frame slicing:** Weapon spritesheets use multiple frame sizes — swords are 64×64 per frame (576×256 = 9×4), but bows and some other weapons use 128×128 per frame (1536×768 = 12×6 or 1024×512 = 8×4). `LPCLayer._update_frame()` hardcoded `layer_hframes = 9` and `layer_vframes = 4` for ALL textures.
2. **Extra attack animation layers:** The `lpc_path_map.json` returns attack animation directories alongside walk/idle textures. `_resolve_asset_bases()` treated any directory containing a PNG as a valid "single_frame" asset, so the Character Creator loaded attack spritesheets as extra layers.

**Files changed:**
- `scripts/LPCLayer.gd` — Complete refactor of frame detection: `_detect_frame_layout()` auto-detects frame size (64/128/192) and layout from actual texture dimensions.
- `scripts/CharacterCreator.gd` — Blocked attack/motion directories with `ANIMATION_DIR_NAMES` constant: `["attack_slash", "attack_thrust", "slash", "thrust", "shoot", "spellcast", "hurt", "climb", "jump", "sit", "emote", "backslash", "halfslash", "combat_idle"]`

**LPC Spritesheet Dimension Reference:**
- Walk: mostly 576×256 (9×4 @ 64px) or 512×256 (8×4 @ 64px), some 1024×512 (8×4 @ 128px) or 1536×768 (12×6 or 8×6 @ 128/192px)
- Idle: 128×256 (2×4 @ 64px)
- Run: 512×256 (8×4 @ 64px)
- Slash/Attack: 384×256 (6×4 @ 64px), 1152×768 (various), 1536×768 (various)
- Hurt: 384×64 (6×1 @ 64px) or 64×64 (1×1 @ 64px)
- Single-frame: 64×64, 128×128, or 192×192

---

## Fix 6b (same session): Weapon jumping left-to-right during idle animation

**Root Cause:** `LPCCharacterAnimator._process()` advances a global frame counter. When a layer doesn't have a texture for the current animation (most weapons have no "idle" spritesheet), `LPCLayer` falls back to its walk texture. The old `set_frame_idx()` was still advancing the walk frame index along with the global counter: walk frame 0 → walk frame 1 → walk frame 0... Walk frame 1 has the arms in a different position than frame 0, so the weapon shifts to the opposite hand.

**Fix:** `LPCLayer.set_frame_idx()` — if layer HAS current animation texture: advance frames normally. If NOT (fallback mode): lock to frame 0 (`current_frame = 0`).

---

## Fix 7 (2026-05-12): Weapon bouncing left-to-right when walking with weapons equipped

**Root Cause:** Many LPC weapons have TWO layers — a foreground layer and a behind layer (`_bg`). The behind layer's spritesheet contains frames NOT in the foreground. When both layers render at the same z_index (0), the behind layer appears ON TOP of the body instead of behind it.

**Fix:** Set `z_index = -1` on all `_bg` (behind) layers so they render behind the body.

**Files changed:**
- `scripts/Player.gd` → `_add_lpc_layer_node()` and `equip_layer()`
- `scripts/OtherPlayer.gd` → `_add_lpc_layer_node()`
- `scripts/CharacterCreator.gd` → `_add_preview_layer()`

**Supporting fixes (same session):**
- `LPCCharacterAnimator._process()`: Use body layer's frame count instead of `layers[0].layer_hframes`
- `LPCCharacterAnimator._gather_layers()`: Skip `queue_free()`'d nodes to prevent stale layer references
- `LPCAssetResolver.load_textures()` and `CharacterCreator._load_textures()`: Handle path map entries where base_path ends in `/walk/` or `/idle/`

---

## Fix 8 (2026-05-13): Large-frame weapons (longsword_alt, katana, scimitar, trident, etc.) hovering above character's hand

**Root Cause:** 128×128 and 192×192 weapon frames have extra padding below the actual weapon content. Standard offset `(-frame_size/2, -frame_size)` placed the weapon too high.

**Fix:** `_update_offset()` normalizes y-offset for larger frames so content bottom aligns with 64×64 body reference:
- 64×64 → `(-32, -64)`
- 128×128 → `(-64, -96)`
- 192×192 → `(-96, -128)`

**File:** `scripts/LPCLayer.gd`

---

## Fix 9 (2026-05-13): Crossbow, wand, rod, whip invisible in Character Creator

**Root Cause (three separate issues):**
1. **Crossbow:** `_load_textures` looked for `walk/background.png` but file is `walk/crossbow.png` — needed directory scan fallback.
2. **Wand:** `_resolve_asset_bases` only checked top-level directory for PNGs. Wand's `male/` only contains `slash/` subdir, so it resolved 0 bases.
3. **Rod/Whip/Crossbow bg:** These spritesheets have empty directions (dir=2/front is completely transparent). `_update_frame()` rendered empty frames.

**Files changed:**
- `scripts/CharacterCreator.gd`: Added `_scan_for_png_recursive()` to scan base dir + subdirectories; added `_subdir_has_png()` for base validation.
- `scripts/LPCLayer.gd`: Added `_find_first_valid_direction()` to pre-compute first non-empty direction at setup time; `_update_frame()` falls back to valid direction when current direction is empty.

---

## Fix 10 (2026-05-13): Rod and whip showing attack/casting sprites while walking

**Root Cause:** These weapons don't have walk/idle/run spritesheets — only attack animations (spellcast/slash). `_scan_for_png_recursive` loaded the attack PNG as "walk" texture, so the animator cycled through casting/lashing frames.

**Fix:** `set_frame_idx()` checks if `layer_hframes` doesn't match the expected frame count for the current animation (walk=9, idle=2, run=8). Mismatch means attack animation loaded as fallback — freeze on frame 0 instead of animating.

**File:** `scripts/LPCLayer.gd`

---

## Fix 11 (2026-05-14): All hats invisible in Character Creator — only trims/buckles/accessories showed up

**Root Cause:** `"hat"` category was completely missing from `UI_GROUPS["Accessories"]` array. `lpc_catalog.json` had 52 hat options (Wizard Hat, Hood, Christmas Hat, Crown, etc.), and `LPC_CATALOG_MAP`/`CAT_BASE_DIRS`/`LAYER_Z_ORDER` were all correctly mapped for `"hat"`. But since it wasn't in `UI_GROUPS`, no UI section ever rendered the hat buttons.

**Fix:** Added `"hat"` to the `Accessories` array in `UI_GROUPS` constant (before `"hat_trim"`).

**File:** `scripts/CharacterCreator.gd`
