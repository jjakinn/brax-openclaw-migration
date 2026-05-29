# 🦾 BRAX OPENCLAW MIGRATION — FINAL MANIFEST

**Archive:** `brax-openclaw-migration.tar.gz` (26MB, 2,908 files)
**Generated:** 2026-05-29
**OpenClaw Version:** 2026.3.2 (LOCKED)
**Based on:** Jakin's complete system

---

## 📦 WHAT'S IN THE PACKAGE

### Core Scripts (6 files)
| Script | Purpose |
|--------|---------|
| `setup.sh` | Main OpenClaw workspace setup — copies all configs, skills, memory, generates openclaw.json |
| `install-tools.sh` | Installs ALL software — 150 Homebrew formulas, 16 npm globals, Ollama models, Rust, Python, Docker |
| `clone-all-repos.sh` | Clones ALL 40+ GitHub repositories with exact remotes |
| `.zshrc.brax` | Complete shell config — all aliases, PATH exports, agent shortcuts |
| `INVENTORY.md` | Complete system inventory — every repo, tool, website, API, config |
| `README.md` | Setup guide and verification steps |
| `TRANSFER.sh` | Transfer helper (how to get this to Brax) |

---

### Workspace Files (9 core .md files)
All copied to `~/.openclaw/workspace/`:
- `MEMORY.md` — Full knowledge base (Brax name substituted)
- `SOUL.md` — Core truths and personality (Brax name substituted)
- `USER.md` — About Brax (Brax name substituted)
- `HEARTBEAT.md` — Automated checks config
- `AGENTS.md` — Super Agent Mode protocols
- `TOOLS.md` — Tool notes, Godot MCP config
- `BOOTSTRAP.md` — First-run guide
- `IDENTITY.md` — Claw's identity
- `CLAUDE.md` — Claude-specific notes

---

### Skills (80 installed)
All copied to `~/.openclaw/workspace/skills/`:
- **Dev:** code, github, data-analysis, gh-issues, session-logs, skill-creator, mcporter, agent-browser, gitnexus
- **Comms:** gmail, google-meet, google-slides, google-workspace-admin, api-gateway, apple-notes, notion, calendly
- **Marketing (30+):** copywriting, ad-creative, email-sequence, cold-email, seo-audit, ai-seo, content-strategy, community-marketing, launch-strategy, competitor-profiling, competitor-alternatives, customer-research, ab-test-setup, analytics-tracking, churn-prevention, directory-submissions, free-tool-strategy, lead-magnets, page-cro, popup-cro, form-cro, signup-flow-cro, onboarding-cro, paywall-upgrade-cro, pricing-strategy, product-marketing-context, programmatic-seo, referral-program, revops, sales-enablement, schema-markup, site-architecture, social-content, aso-audit, video-frames, weather, web-search, humanizer
- **Infra:** auto-updater, heartbeat, healthcheck, clawhub, free-ride, smart-cache-router
- **Other:** peekaboo, video-frames, desktop-control, agent-phone-call, polymarket-trade, n8n-workflow-automation, x-twitter, youtube-watcher, openclaw-youtube-transcript, imap-smtp-email, outlook-api, typeform, microsoft-excel, shopify, discord, answeroverflow, multi-search-engine, pdf, word-docx, image

---

### Memory Archive (50+ daily logs)
All copied to `~/.openclaw/workspace/memory/`:
- Daily logs from 2026-03-18 through 2026-05-28
- Every session, fix, decision, and learned pattern

---

### n8n Workflows (11 files)
All copied to `~/n8n-workflows/`:
- `token-monitor.json` — Alert at 75% token usage
- `error-handler.json` — Route failures to review queue
- `daily-digest.json` — Daily metrics email
- `clawmind-auto-learning.json` — Auto-learning pipeline
- `clawmind-conversation-capture.json` — Conversation capture
- `clawmind-error-handler.json` — Error handling
- `clawmind-gap-finder.json` — Gap analysis
- `clawmind-simple.json` — Simple workflow
- `test-simple.json` — Test workflow
- `CLAWMIND-README.md` — Documentation
- `config.md` — Configuration guide

---

### Self-Improving System (full stack)
All copied to `~/self-improving/`:
- `memory.md` — HOT memory
- `corrections.md` — Recent corrections
- `reflections.md` — Self-reflections
- `heartbeat-state.md`, `index.md`
- `archive/` — COLD memory
- `domains/` — Domain patterns
- `drafts/` — Draft patterns
- `projects/` — Project patterns
- `snapshots/` — Memory snapshots

---

### Data Analysis Setup
All copied to `~/data-analysis/`:
- `config.md` — Analysis configuration
- `datasets/` — Data folders
- `reports/` — Generated reports

---

## 🔑 KEY DIFFERENCES (JAKIN → BRAX)

| Feature | Jakin | Brax |
|---------|-------|------|
| Name | Jakin | Brax (auto-substituted) |
| Telegram | Enabled | **DISABLED** (webchat only) |
| Kimi API | Jakin's key | **Brax configures his own** |
| Brave Search | Jakin's key | **Brax configures his own** |
| GitHub Token | Jakin's PAT | **Brax generates his own** |
| Gateway Token | Jakin's | **Auto-generated placeholder** |
| Git Config | jakin@purifoy.org | **brax@example.com** (update) |

---

## 🚀 BRAX'S SETUP ORDER

```bash
# 1. Extract archive
tar -xzf brax-openclaw-migration.tar.gz
cd brax-migration

# 2. Install ALL tools (takes 30-60 min)
./install-tools.sh

# 3. Clone ALL repos (takes 10-20 min)
./clone-all-repos.sh

# 4. Set up OpenClaw workspace
./setup.sh

# 5. Copy shell config
cp .zshrc.brax ~/.zshrc
source ~/.zshrc

# 6. Configure API keys
openclaw auth add kimi-coding    # Paste Brax's Kimi key
# Edit ~/.openclaw/openclaw.json → replace YOUR_BRAVE_API_KEY_HERE

# 7. Start gateway
openclaw gateway start

# 8. Open webchat
open http://localhost:18789
```

---

## 📊 REPOSITORIES TO CLONE (40+)

### OpenClaw / AI Infra
- GitNexus, GitNexus Tool, Hermes, Godot MCP

### Club Penguin / Game Dev (16 repos)
- ClubPenguin, cpadvanced-client, cp-swf, cp-minigames, cpps-houdini, cpps-mammoth, waddle-forever, yukon-client, yukon-server, project-aether, flipper-client, flipper-island, lpc-generator, etc.

### AI / ML / Generative (9 repos)
- ComfyUI, CubeSandbox, Decepticon, Hunyuan3D, HunyuanImage, HunyuanVideo, docker-android, ai4animationpy, lyra

### SaaS / API Projects (9 repos)
- SSL Analyzer, Breach Checker, IP Reputation, Leadvault Automation, Leadvault Site, Rize Clone, fly-brain, terminalphone, TitanEngine

### Other / Utility (20+ repos)
- pyenv, CL1_LLM_Encoder, CADAM, PLFM_RADAR, the_well, dimos, asimov-v0, modly, OBLITERATUS, Claw3D, carbonyl, fff.nvim, openscreen, claw-code, try-html-in-canvas, editor, stenoai, RuView, tuitter

---

## 🛠️ TOOLS INSTALLED (150+ Brew + 16 NPM + Ollama + Rust + Python)

### Critical Brew Packages
- `gh`, `git`, `node@22`, `python@3.14`, `pyenv`, `deno`, `docker`, `docker-compose`, `colima`, `lima`, `redis`, `mysql`, `postgresql@16`, `sqlite`, `gcc`
- `ffmpeg`, `imagemagick`, `vips`, `ollama`, `mlx`, `cloudflared`, `gnupg`, `ripgrep`, `htop`, `yt-dlp`, `ngrok`

### NPM Global
- `openclaw@2026.3.2`, `n8n@2.15.0`, `pnpm`, `yarn`, `vercel`, `clawhub`, `mcporter`, `agent-browser`, `create-next-app`, `@railway/cli`, `@microsoft/power-apps-cli`

### Ollama Models
- llama3.2:3b, dolphin-uncensored, dolphin3:8b, qwen2.5-coder:7b, qwen2.5:7b, nous-hermes2, dolphin-llama3:8b, glm-4.7-flash

### Other
- Rust (via rustup), UV (Python package manager), Conda/Miniconda

---

## 🔗 WEBSITES / APIs / SERVICES REFERENCED

### Bug Bounty
bugcrowd.com, hackerone.com, intigriti.com, openbugbounty.org, yeswehack.com, disclose/diodb

### APIs / Services
ssl-analyzer-api.onrender.com, api.search.brave.com, api.kimi.com, discord webhooks, crt.sh, web.archive.org, seostudio.tools, cobalt.tools, barkod.studio, animejs.com

### Hosting / Cloud
fly.io, railway.app, vercel.com, render.com, ngrok.com, cloudflare.com

### GitHub Referenced (Not Cloned)
30+ additional repos for reference (listed in INVENTORY.md)

---

## ⚠️ SECRETS (NOT INCLUDED — BRAX MUST CONFIGURE)

| Secret | How to Obtain |
|--------|---------------|
| Kimi API Key | https://platform.moonshot.cn |
| Brave Search API Key | https://api.search.brave.com (free) |
| GitHub PAT | GitHub Settings → Developer → PAT |
| Fly.io Token | `fly auth login` |
| Railway Token | `railway login` |
| Vercel Token | `vercel login` |
| Ngrok Auth | https://dashboard.ngrok.com |
| OpenClaw Gateway Token | `openssl rand -hex 20` |

---

## ✅ VERIFICATION CHECKLIST

After setup, verify:
```bash
openclaw --version          # 2026.3.2
ls ~/.openclaw/workspace/skills | wc -l     # ~80
ls ~/.openclaw/workspace/memory | wc -l     # ~50
ls ~/n8n-workflows          # 11 files
ls ~/self-improving         # Full structure
ls ~/data-analysis          # config.md, datasets, reports
brew list | wc -l           # ~150
npm list -g --depth=0 | wc -l   # ~16
ollama list | wc -l         # ~12 models
ls ~/bin                    # terminalphone
ls ~/.local/bin             # hermes, uv, uvx, kimi
```

---

**🎉 Package is complete and ready to transfer to Brax.**
