# 🦆 VIVID TUI

Branded terminal UI for the VIVID Agent.

## Quick Start

```bash
# If you already have OpenClaw installed and gateway running:
npx vivid-tui

# Or start the gateway automatically:
npx vivid-tui --start
```

## What It Does

1. Shows the 🦆 VIVID Agent banner
2. Checks if your OpenClaw gateway is running
3. Connects you to the full OpenClaw TUI experience
4. Custom VIVID-themed colors and branding

## Commands (in chat)

| Command | Description |
|---------|-------------|
| `/help` or `/h` | Show help |
| `/quit` or `/q` | Exit VIVID |
| `/clear` or `/c` | Clear screen |
| `/status` | Check gateway status |

## Installation

Comes pre-installed with the VIVID Agent Setup. If you need it separately:

```bash
cd vivid-tui
npm install -g .
```

Then run `vivid-tui` or `vivid` from anywhere.

## Requirements

- OpenClaw 2026.3.2 installed
- Gateway running on localhost:18789 (or start with --start)

---

Built for VIVID Agent 🦆
