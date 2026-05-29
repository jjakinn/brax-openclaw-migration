# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## Godot MCP Server

**Installed:** `~/godot-mcp/` — MCP server for Godot engine control  
**Godot Path:** `/Users/Jakin/Downloads/Godot.app/Contents/MacOS/Godot`  
**Config:** `~/.openclaw/workspace/config/mcporter.json`  
**Version:** 4.6.2.stable

### Usage (via mcporter)

```bash
# List available tools
mcporter list godot --schema

# Launch Godot editor
mcporter call godot.launch_editor projectPath="/path/to/project"

# Run project and capture debug output
mcporter call godot.run_project projectPath="/path/to/project"

# Get debug output from running project
mcporter call godot.get_debug_output

# Stop running project
mcporter call godot.stop_project

# Get Godot version
mcporter call godot.get_godot_version

# List projects in directory
mcporter call godot.list_projects directory="~/godot-projects"

# Create a new scene
mcporter call godot.create_scene projectPath="/path/to/project" scenePath="scenes/Player.tscn" rootNodeType="Node2D"

# Add node to scene
mcporter call godot.add_node projectPath="/path/to/project" scenePath="scenes/Player.tscn" nodeType="Sprite2D" nodeName="Body"

# Load sprite texture
mcporter call godot.load_sprite projectPath="/path/to/project" scenePath="scenes/Player.tscn" nodePath="root/Body" texturePath="assets/player.png"
```

### Available Tools (14 total)

- `launch_editor` — Open Godot editor for project
- `run_project` — Run project in debug mode
- `get_debug_output` — Get console output/errors
- `stop_project` — Stop running project
- `get_godot_version` — Get installed Godot version
- `list_projects` — Find Godot projects in directory
- `get_project_info` — Get project metadata
- `create_scene` — Create new .tscn scene file
- `add_node` — Add node to existing scene
- `load_sprite` — Load texture into Sprite2D
- `export_mesh_library` — Export scene as MeshLibrary
- `save_scene` — Save scene changes
- `get_uid` — Get UID for file (Godot 4.4+)
- `update_project_uids` — Resave resources to update UIDs

---

Add whatever helps you do your job. This is your cheat sheet.
