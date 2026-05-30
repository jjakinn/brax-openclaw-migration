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
- **Git Repository:** Initialized local git repo. No remote configured.
- **Known Good Commit:** `399d9be` — "Fix color mismatch: remove shader fallback that was double-recoloring pixels"
- **Previous Good Commit:** `9541cb1` — "Fix color mismatch: use CPU-side palette recoloring in-game (matching preview)"
- **Full Fix Log:** See `memory/archive/galaxy-demo-fixes.md` (11 fixes from 2026-05-11 to 2026-05-14)

### Interests
- Workflow automation
- AI integration
- Exploring OpenClaw capabilities
- Token optimization and cost management
- Online casino affiliate business
- Marketing skills and CRO/copywriting/SEO automation

---

## Active Projects

### 🧠 ClawMind / My Digital Brain (Memory System - Active)
- **Concept:** Persistent memory as a knowledge graph
- **Location:** `~/ClawMind/`
- **Structure:** Index.md dashboard + linked notes on identity, capabilities, projects, knowledge, daily notes
- **How to Open:** Install Obsidian → "Open folder as vault" → `~/ClawMind/` → Graph view
- **Status:** Active primary memory system

### 🌍 World Monitor (Custom Desktop App - BUILT & WORKING)
- **Status:** Built and working with 100% free APIs
- **Location:** `~/Desktop/world-monitor-custom/`
- **Details:** `memory/projects/world-monitor.md`

### 🧠 FlyBrainAI / Claw v5 (Self-Aware Neural Agent - Active)
- **Status:** v5 implemented — obeys commands, internal mode, self-analyzes, non-performative
- **Location:** `~/fly-brain/`
- **Details:** `memory/projects/flybrain-ai.md`

### 🎯 LASER Browser (Innovation/Breakthrough - In Progress)
- **Concept:** AI-Native Browser Control with 10x precision over screenshot automation
- **Solution:** LASER Architecture — WebSocket state streaming, CDP, accessibility tree, consensus matching, verification layer
- **Performance:** 50-100ms latency, 99%+ precision, <1% error rate
- **Files:** `/Users/Jakin/.openclaw/workspace/laser-browser/` + skill at `skills/laser-browser/SKILL.md`
- **Status:** Phase 1 Complete (Foundation)

### 🥊 UFC Gematria v3 — Ultimate Deep Analysis (Active)
- **Status:** Production-ready. 10 integrated analysis sections.
- **Location:** `~/.openclaw/workspace/ufc-gematria/`
- **Details:** `memory/projects/ufc-gematria.md`

### 🎰 Casino Build Plan (Waiting to Build)
- **Concept:** Branded affiliate casino frontend — Jakin's own brand/domain/logos as a casino site, but every action routes to Rainbet

### ⚡ Power Apps Code Apps - Development Workflow
- **Details:** `memory/technical/power-apps-development.md`

### Mission Control Dashboard
- **Status:** Operational
- **URL:** http://localhost:3001
- **Stack:** Next.js, React, TypeScript, Tailwind
- **Features:** Task Board, Token Tracker, Calendar, Projects, Memories, Documents, Team, Office, Live Activity Feed

### 🛠️ API Business — Build & Sell Plan (2026-05-20)
- **Status:** ACTIVE — building 13 API products across 3 phases
- **Goal:** $4,000/month recurring via RapidAPI + direct sales
- **Full catalog:** `~/ClawMind/API Business Catalog — Build & Sell Plan.md`
- **Build playbook:** `~/ClawMind/API Build & Sell Playbook.md`
- **First API DEPLOYED ✅:** SSL/TLS Config Analyzer — https://ssl-analyzer-api.onrender.com — listed on RapidAPI (2026-05-20)
- **Build Order:** Email/Domain Breach Checker (next) → Subdomain Enumerator → IP Reputation Check → Nuclei Template Runner → Website Screenshot + Tech Detector → Meeting Transcript → Action Items → Document Parser (OCR) → Business Entity Lookup → Real Estate Data Aggregator → Social Post Generator → Crypto Wallet Labeler
- **Key Principle:** "You don't need to be original. You just need to be useful."

### Token Management
- **Checkpoint at 78%** (~204k tokens) — Save progress, create checkpoint file, automatically spawn continuation agent
- **Resume:** New agent auto-continues from checkpoint seamlessly
- **Strategy:** Work until 78%, checkpoint, spawn continuation agent, halt

---

## Technical Setup

### Models Configured
- **Primary:** kimi-coding/k2p5 (262k context)
- **Heartbeat:** ollama/llama3.2 (free, local)

### Free Tool Resources
- **SEO Studio Tools:** https://seostudio.tools — Collection of free SEO/web tools. Check here first before paid alternatives.
- **Full Tools Catalog:** See `memory/archive/tools-catalog.md` (30+ saved tools across dev, 3D, AI, robotics, productivity, trading, CP resources)

### Permissions Granted
- Terminal: Accessibility permissions (desktop control)
- Safari: JavaScript from Apple Events enabled

### Key Integrations
- YouTube Watcher (transcripts)
- Desktop Control (UI automation)
- Brave Search API

---

## Important Decisions

### OpenClaw Version Compatibility
- **Current:** OpenClaw 2026.3.2 (build 85377a2)
- **Status:** BEST version for kimi-coding/k2p5 — tool calling works correctly
- **⚠️ Warning:** Other updates break kimi tool calling — DO NOT upgrade until confirmed fixed
- **If kimi tool calling breaks:** Delete `~/.openclaw/nano.json`, reinstall 2026.3.2, restart — memory/soul files are preserved

### Security Boundaries
- Private data stays private
- No autonomous external posting
- Destructive commands: always ask first
- Prefer `trash` over `rm`

---

## Marketing Skills
- **Source:** https://github.com/coreyhaines31/marketingskills (installed 2026-04-29)
- **Count:** 40 marketing skills installed
- **Foundation skill:** `product-marketing-context` (read by all other skills first)
- **Categories:** CRO, Copy & Content, SEO, Paid & Analytics, Growth & Retention, Sales & RevOps, Strategy & Research
- **How they work:** Markdown files that give AI agents specialized knowledge and workflows for specific marketing tasks
- **Install command used:** Clawhub CLI via `cp -r /tmp/marketingskills/skills/* /Users/Jakin/.openclaw/workspace/skills/`
- **Next step:** Create `.agents/product-marketing-context.md` or update `.claude/product-marketing-context.md` with Jakin's product info

---

## Lessons Learned (Key)

- Desktop control requires accessibility permissions
- JavaScript Apple Events more reliable than UI coordinates
- Token checkpointing = unlimited work across sessions (78% → new agent → seamless resume)
- Direct URLs better than UI clicking for web automation
- **NEVER auto-update OpenClaw without testing kimi first** — 2026.3.2 is the known-good build
- Knowledge graph with cross-references enables synthesis across sources

---

## Archives

- **Godot Fix Log:** `memory/archive/galaxy-demo-fixes.md` (11 detailed fixes)
- **Transcript Ingestions:** `memory/archive/transcript-ingestions.md` (50+ video transcripts, Liam Ottley series, Starter Story)
- **Tools Catalog:** `memory/archive/tools-catalog.md` (30+ saved tools and resources)
- **Original Transcript Archive:** `memory/archive/TRANSCRIPT_ARCHIVE_2026-04-21.md` (50+ older transcripts)
- **ClawMind Vault:** All actual transcript files are in `~/ClawMind/` as standalone .md files
