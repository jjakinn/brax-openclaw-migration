# 🦾 OpenClaw Migration Package — Brax Setup

**Source:** Jakin's exact setup (OpenClaw 2026.3.2)
**Version locked:** 2026.3.2 (NOT newer)
**Date:** 2026-05-29

---

## 📦 What's In This Package

This is a **complete, byte-for-byte clone** of Jakin's OpenClaw environment with only these changes:
- `Jakin` → `Brax` in MEMORY.md, SOUL.md, USER.md
- Telegram removed (webchat only)
- Your own Kimi subscription (you add your own API key)
- Paths auto-adjusted to your home directory

### Included

| Component | Description | Count/Status |
|-----------|-------------|--------------|
| **OpenClaw Version** | Locked to `2026.3.2` | Exact same build |
| **Workspace Files** | MEMORY, SOUL, USER, HEARTBEAT, AGENTS, TOOLS, BOOTSTRAP, IDENTITY, CLAUDE | 9 core files |
| **Skills** | All installed skills (code, github, data-analysis, n8n, marketing, CRO, etc.) | 80 skills |
| **Memory Archive** | Daily memory logs from 2026-03-18 through 2026-05-28 | 50 files |
| **n8n Workflows** | Token monitor, error handler, daily digest, ClawMind automations | 11 workflows |
| **Self-Improving System** | HOT/WARM/COLD memory tiers, corrections, reflections, project patterns | Full setup |
| **Data Analysis** | Config, datasets folder, reports folder | Ready to use |
| **Super Agent Config** | AGENTS.md with GitNexus, n8n, data analysis, self-improving protocols | Active |

---

## 🚀 Quick Start

### 1. Install Node.js/npm (if not already)

```bash
# macOS (Homebrew)
brew install node

# Linux
sudo apt update && sudo apt install -y nodejs npm

# Verify
node --version  # v18+ required
npm --version
```

### 2. Install OpenClaw 2026.3.2 (Exact Version)

```bash
npm install -g openclaw@2026.3.2
```

**Verify:**
```bash
openclaw --version
# Should print: 2026.3.2
```

### 3. Run the Setup Script

```bash
cd brax-migration
chmod +x setup.sh
./setup.sh
```

This will:
- Create `~/.openclaw/workspace/` with all files
- Copy all 80 skills
- Copy all memory archives
- Copy n8n workflows to `~/n8n-workflows/`
- Copy self-improving system to `~/self-improving/`
- Copy data analysis setup to `~/data-analysis/`
- Generate `~/.openclaw/openclaw.json` with your paths
- Replace `Jakin` → `Brax` in MEMORY.md, SOUL.md, USER.md

### 4. Configure Your API Keys

#### Kimi (Required)
```bash
openclaw auth add kimi-coding
# Paste your Kimi API key when prompted
```

#### Brave Search (Required for web search)
Edit `~/.openclaw/openclaw.json`:
```json
"tools": {
  "web": {
    "search": {
      "enabled": true,
      "apiKey": "YOUR_BRAVE_API_KEY_HERE"
    },
    "fetch": {
      "enabled": true
    }
  }
}
```
Get a free key at: https://api.search.brave.com/app/dashboard

#### Gateway Token (Optional but recommended)
Generate a new random token:
```bash
openssl rand -hex 20
```
Then replace `GENERATE_NEW_TOKEN` in `~/.openclaw/openclaw.json` → `gateway.auth.token`

---

## ✅ What You'll Have (Identical to Jakin)

### Super Agent Mode
- **Self-Improving Agent** — Learns from every interaction, logs corrections, promotes repeated patterns
- **GitNexus** — Code intelligence for all coding tasks (impact analysis, change detection, safe refactoring)
- **n8n Automation** — Token monitor, error handler, daily digest workflows ready to import
- **Data Analysis** — SQL, Python, visualization stack with decision-brief output format

### All 80 Skills
Including but not limited to:
- `code` — Full coding workflow with planning, implementation, verification, testing
- `github` — GH CLI operations (issues, PRs, CI, code review)
- `data-analysis` — SQL, Python, visualization, statistical rigor
- `gh-issues` — Fetch issues, spawn sub-agents to fix, monitor PR reviews
- `session-logs` — Search and analyze conversation logs with jq
- `skill-creator` — Create/update AgentSkills
- `mcporter` — MCP server management (including Godot MCP)
- `agent-browser` — Headless browser automation
- `gmail`, `google-meet`, `google-slides`, `google-workspace-admin`
- `api-gateway` — Maton.ai OAuth for 100+ APIs
- `apple-notes`, `notion`, `calendly`
- All marketing skills: `copywriting`, `ad-creative`, `email-sequence`, `cold-email`, `seo-audit`, `ai-seo`, `content-strategy`, `community-marketing`, `launch-strategy`, `competitor-profiling`, `competitor-alternatives`, `customer-research`, `ab-test-setup`, `analytics-tracking`, `churn-prevention`, `directory-submissions`, `free-tool-strategy`, `lead-magnets`, `page-cro`, `popup-cro`, `form-cro`, `signup-flow-cro`, `onboarding-cro`, `paywall-upgrade-cro`, `pricing-strategy`, `product-marketing-context`, `programmatic-seo`, `referral-program`, `revops`, `sales-enablement`, `schema-markup`, `site-architecture`, `social-content`, `aso-audit`, `video-frames`, `weather`, `web-search`, `humanizer`
- All CRO/optimization skills
- All OpenClaw infrastructure skills: `auto-updater`, `heartbeat`, `healthcheck`, `clawhub`

### Memory System
- 50 days of memory archives in `~/.openclaw/workspace/memory/`
- Full Galaxy Demo Godot project knowledge (fixes, patterns, sprite system)
- Casino build plan, bug bounty strategies, SaaS ideas
- All learned patterns, corrections, and project notes

### Godot MCP Integration
- Full Godot 4.6.2 MCP server config in TOOLS.md
- Scene creation, node addition, sprite loading, project management
- **Note:** You'll need to install Godot 4.6.2 and the MCP server separately if you want this

### n8n Workflows
Located in `~/n8n-workflows/`:
- `token-monitor.json` — Alert at 75% token usage
- `error-handler.json` — Route failures to review queue
- `daily-digest.json` — Daily metrics email
- `clawmind-auto-learning.json` — Auto-learning pipeline
- `clawmind-conversation-capture.json` — Conversation capture
- `clawmind-error-handler.json` — Error handling
- `clawmind-gap-finder.json` — Gap analysis
- `clawmind-simple.json` — Simple workflow
- Plus config and test files

---

## 🔧 Post-Install Verification

Run these commands to verify everything:

```bash
# 1. Check OpenClaw version
openclaw --version
# Expected: 2026.3.2

# 2. Check skills
ls ~/.openclaw/workspace/skills/ | wc -l
# Expected: ~80

# 3. Check memory
ls ~/.openclaw/workspace/memory/ | wc -l
# Expected: ~50

# 4. Check workspace files
ls ~/.openclaw/workspace/*.md
# Expected: AGENTS.md, BOOTSTRAP.md, CLAUDE.md, HEARTBEAT.md, IDENTITY.md, MEMORY.md, SOUL.md, TOOLS.md, USER.md

# 5. Check self-improving
ls ~/self-improving/
# Expected: archive, corrections.md, domains, drafts, heartbeat-state.md, index.md, memory.md, projects, reflections.md, snapshots

# 6. Check n8n workflows
ls ~/n8n-workflows/
# Expected: *.json files and config.md

# 7. Start gateway
openclaw gateway start
# Then open http://localhost:18789
```

---

## ⚠️ What's Different (On Purpose)

| Feature | Jakin | Brax (You) |
|---------|-------|-----------|
| Name | Jakin | Brax (auto-replaced) |
| Telegram | Enabled | **Disabled** (webchat only) |
| Kimi API Key | Jakin's | **Your own** (you configure) |
| Brave Search Key | Jakin's | **Your own** (you configure) |
| Gateway Token | Jakin's | Auto-generated placeholder |
| Godot Path | `/Users/Jakin/...` | **You update in TOOLS.md** |
| Home Directory | `/Users/Jakin` | **Auto-detected as `$HOME`** |

---

## 📋 File Structure After Install

```
~/.openclaw/
├── openclaw.json          # Your config (Kimi, gateway, tools)
└── workspace/
    ├── MEMORY.md          # Full memory (Brax's name)
    ├── SOUL.md            # Core truths (Brax's name)
    ├── USER.md            # About you (Brax's name)
    ├── HEARTBEAT.md       # Automated checks config
    ├── AGENTS.md          # Super Agent Mode protocols
    ├── TOOLS.md           # Your tool notes (update Godot path)
    ├── BOOTSTRAP.md       # First-run guide
    ├── IDENTITY.md        # Claw's identity
    ├── CLAUDE.md          # Claude-specific notes
    ├── memory/            # 50 days of archives
    ├── skills/            # 80 installed skills
    └── config/
        └── mcporter.json  # MCP server config

~/self-improving/
├── memory.md              # HOT memory
├── corrections.md         # Recent corrections
├── reflections.md         # Self-reflections
├── heartbeat-state.md
├── index.md
├── archive/               # COLD memory
├── domains/               # Domain-specific patterns
├── drafts/                # Draft patterns
├── projects/              # Project-specific patterns
└── snapshots/             # Memory snapshots

~/n8n-workflows/
├── token-monitor.json
├── error-handler.json
├── daily-digest.json
├── clawmind-*.json
└── config.md

~/data-analysis/
├── config.md
├── datasets/
└── reports/
```

---

## 🔒 Security Notes

- **No secrets in this package** — All API keys are placeholders
- **No Telegram bot token** — Telegram is completely disabled
- **No OpenClaw gateway auth token** — You generate your own
- **Webchat only** — No messaging channels pre-configured
- **Kimi subscription is yours** — You use your own API key, billing is separate

---

## 🆘 Troubleshooting

### "openclaw: command not found"
```bash
# Make sure npm global bin is in PATH
export PATH="$PATH:$(npm bin -g)"
# Or reinstall
npm install -g openclaw@2026.3.2
```

### Skills not showing up
```bash
# Re-scan skills
openclaw skills check
```

### Kimi not working
```bash
# Verify auth
openclaw auth list
# Re-add if needed
openclaw auth add kimi-coding
```

### Gateway won't start
```bash
# Check config
openclaw config validate
# Or regenerate
openclaw configure
```

---

## 📞 Support

If something breaks, the error logs are your friend:
```bash
openclaw logs
```

Or check the session logs:
```bash
openclaw session-logs list
```

---

**Built with 💀 by Jakin for Brax**
**OpenClaw 2026.3.2 — Exact Version Locked**
