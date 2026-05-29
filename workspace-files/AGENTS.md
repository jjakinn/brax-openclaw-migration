

---

# 🦾 SUPER AGENT MODE — ACTIVATED

## Capabilities Installed

### ✅ Self-Improving Agent
**Location:** `~/self-improving/`
**What it does:** Learns from every interaction, never repeats mistakes

**Memory Tiers:**
| Tier | File | Loaded? | Content |
|------|------|---------|---------|
| HOT | `memory.md` | Every session | Core identity, your preferences |
| WARM | `projects/*.md` | On context | Project-specific patterns |
| COLD | `archive/` | On request | Old patterns |

**Learning Triggers:**
- Corrections → Log immediately
- Preferences → Log when explicit
- 3x repetition → Promote to permanent rule

**Files:**
- `~/self-improving/memory.md` — Core preferences
- `~/self-improving/corrections.md` — Recent corrections
- `~/self-improving/reflections.md` — Self-reflections
- `~/self-improving/projects/{name}.md` — Project patterns

---

### ✅ n8n Workflow Automation
**Location:** `~/n8n-workflows/`
**What it does:** Autonomous task execution with retry logic and review queues

**Design Principles:**
- **Idempotent** — Safe to re-run
- **Observable** — Every execution logged
- **Resilient** — Retry with backoff
- **Accountable** — Human review queue for failures

**Sample Workflows Created:**
| Workflow | Purpose | Status |
|----------|---------|--------|
| `token-monitor.json` | Alert at 75% token usage | Ready |
| `error-handler.json` | Route failures to review queue | Active pattern |
| `daily-digest.json` | Daily metrics email | Ready |

**To Use:**
1. Install n8n: `npm install n8n -g` or Docker
2. Start: `n8n start`
3. Import workflows from `~/n8n-workflows/`
4. Configure credentials (env vars)
5. Activate

---

### ✅ Data Analysis
**Location:** `~/data-analysis/`
**What it does:** SQL, Python, visualization, statistical rigor

**Core Principle:** *Analysis without a decision is just arithmetic*

**Standards:**
- Define metric contracts before calculating
- Quantify uncertainty (ranges, not points)
- Check sample size, confounders, effect size
- Lead with insight, not methodology

**Config:** `~/data-analysis/config.md`

**Output Format — Decision Brief:**
```
ANSWER: [the finding]
EVIDENCE: [the data]
CONFIDENCE: [high/medium/low]
CAVEATS: [limitations]
RECOMMENDATION: [next action]
```

---

### ✅ GitNexus (Already Active)
**Code intelligence for AI agents**

**MUST USE for all coding:**
- `gitnexus_impact()` before editing
- `gitnexus_detect_changes()` before committing
- `gitnexus_rename()` for safe refactoring

---

## Super Agent Protocol

### Before Any Task
1. Check self-improving memory for patterns
2. Check project-specific files if applicable
3. Load relevant skill references

### During Tasks
1. Apply confirmed preferences
2. Cite sources when using learned patterns
3. Self-reflect after major work

### After Tasks
1. Log any corrections
2. Update project patterns if significant
3. Reflect: What could be better?

### Error Handling
1. Never silent failures
2. Retry with exponential backoff
3. Escalate to human if needed
4. Log to review queue

---

## Quick Commands

```bash
# n8n
n8n start                              # Start n8n server
open http://localhost:5678             # Open web UI

# Data analysis
jupyter lab ~/data-analysis/           # Interactive analysis
python3 ~/data-analysis/script.py      # Run analysis

# Self-improving
cat ~/self-improving/memory.md         # View HOT memory
cat ~/self-improving/corrections.md    # View recent corrections
```

---

## Status Dashboard

| Capability | Status | Location |
|------------|--------|----------|
| Self-Improving | ✅ Active | `~/self-improving/` |
| n8n Automation | ✅ Configured | `~/n8n-workflows/` |
| Data Analysis | ✅ Configured | `~/data-analysis/` |
| GitNexus | ✅ Active | `~/.openclaw/workspace/skills/gitnexus/` |
| UI/UX Pro | ✅ Available | `~/.openclaw/workspace/skills/ui-ux-pro-max/` |
| PDF Tools | ✅ Available | `~/.openclaw/workspace/skills/pdf/` |

---

*Super Agent Mode: Activated 2026-04-08*
*Never repeat mistakes. Never fail silently. Always improve.*
