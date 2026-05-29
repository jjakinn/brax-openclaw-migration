# Synthesis: OpenClaw Mastery
*Cross-reference from 10+ sources covering setup, workflows, multi-agent systems, and monetization*

---

## Core Architecture

**What OpenClaw Is:**
An AI agent framework that gives language models access to tools, memory, and persistent state — enabling autonomous task execution.

**Key Components:**
1. **Agent** — AI with instructions, tools, and memory
2. **Skills** — Reusable tool packages (GitHub, browser, desktop control)
3. **Sessions** — Persistent conversations with context
4. **Knowledge Graph** — Structured memory for information retrieval

---

## Setup Best Practices

### Version Lock (Critical)

> "OpenClaw 2026.3.2 (build 85377a2) is the BEST version for kimi right now. Other updates break kimi tool calling."

**If tool calling breaks:**
```bash
# Nuclear option — preserves memory/soul
rm ~/.openclaw/nano.json
# Reinstall 2026.3.2
# Restart — memory files survive
```

### Model Configuration

**Recommended Setup:**
```json
{
  "primary_model": "kimi-coding/k2p5",
  "heartbeat_model": "ollama/llama3.2",
  "checkpoint_threshold": 0.78
}
```

**Why kimi-coding/k2p5:**
- 262k context window
- Excellent tool calling
- Cost-effective for long sessions

**Token Checkpointing:**
- Work until 78% (~204k tokens)
- Create checkpoint
- Spawn continuation agent
- New agent resumes seamlessly

---

## Skill Ecosystem

### Essential Skills for Security Work

| Skill | Purpose | Use Case |
|-------|---------|----------|
| **github** | Issues, PRs, CI runs | Code review, automation |
| **browser** | Headless automation | Web recon, form submission |
| **desktop-control** | Mouse/keyboard | UI automation, internal tools |
| **peekaboo** | macOS UI capture | Screenshot workflows |
| **agent-browser** | Advanced browser control | Complex web interactions |

### For AI/ML Work

| Skill | Purpose |
|-------|---------|
| **youtube-watcher** | Transcript extraction |
| **web-search** | DuckDuckGo search |
| **multi-search-engine** | 17 engines (8 CN + 9 Global) |
| **pdf** | Document analysis |
| **image** | Vision model analysis |

### For Automation

| Skill | Purpose |
|-------|---------|
| **n8n-workflow-automation** | Workflow design |
| **calendly** | Scheduling integration |
| **gmail** | Email automation |
| **outlook** | Microsoft email/calendar |

---

## Multi-Agent Architecture

### Pattern: Agent Army

**From Alex Finn — "Build an Army of OpenClaw Agents":**

**Types of Agents:**
1. **Research Agent** — Gathers information
2. **Analysis Agent** — Processes findings
3. **Action Agent** — Executes tasks
4. **Review Agent** — Validates output

**Communication:**
- Agents share context through MEMORY.md
- Task queues in `memory/workflows/task-queue.md`
- Checkpoints enable handoffs

### Pattern: Specialized Workers

**From Mani Kanasani — "5 AI Employees":**

| Role | Function |
|------|----------|
| **Researcher** | OSINT, competitive analysis |
| **Writer** | Content creation, documentation |
| **Coder** | Development, debugging |
| **Analyst** | Data processing, insights |
| **Manager** | Task orchestration |

---

## Knowledge Graph Best Practices

### Ingestion Protocol

**Trigger:** User says **"ingest"**

**Process:**
1. Drop files/videos in `library/inbox/`
2. Chunk content
3. Index by source + by concept
4. Cross-reference related concepts
5. Update master catalog

**Structure:**
```
memory/knowledge-graph/
├── corpus/
│   ├── by-source/{source-id}/
│   │   ├── metadata.json
│   │   └── chunks/chunk_001.txt
│   └── by-concept/
│       ├── {concept-id}.json
│       └── syntheses/{concept-id}.md
├── ontology/
│   ├── prerequisites.json
│   └── domains.json
└── index/
    └── master-catalog.md
```

### Query Protocol

1. **Check library FIRST**
2. Cross-reference multiple sources
3. Cite exact quotes with sources
4. Flag knowledge gaps
5. Fall back to general knowledge ONLY if library silent

---

## Workflow Optimization

### Local LLM Integration (Ollama)

**From NetworkChuck:**

**Setup:**
```bash
brew install ollama
ollama pull qwen2.5-coder:8b
```

**Recommended Models:**
| Model | VRAM | Best For |
|-------|------|----------|
| Qwen 2.5 Coder 3B | ~4GB | Lightweight tasks |
| Qwen 2.5 Coder 8B | 11GB | Balanced |
| Qwen 2.5 Coder 14B | ~18GB | Better accuracy |
| Qwen 2.5 Coder 32B | ~35GB | Highest accuracy |

**Claude Code Integration:**
```bash
claude --config
# Select Ollama model from menu
```

**Cloud Alternative (Free):**
- **GLM-4.7** (Zhipu AI)
- 250,000 input tokens/hour free
- Better accuracy than local 8B models

### Storybook Pattern for Local Models

**Strategy:**
- Break UI into single components
- Perfect one component at a time
- Less context = better local model performance

```bash
npx storybook@latest init
```

---

## Security & Hardening

### Permissions Required

| Task | Permission |
|------|------------|
| Desktop control | Accessibility (System Settings) |
| Browser automation | JavaScript from Apple Events |
| File system | Full disk access (if needed) |

### Safe Defaults

- `trash` > `rm` (recoverable)
- Ask before destructive commands
- Private data stays private
- No autonomous external posting

---

## Monetization Strategies

### From Greg Isenberg — "Making $$$ with OpenClaw":

**Service Models:**
1. **Automation Agency** — Build workflows for clients
2. **Content at Scale** — AI-assisted research + writing
3. **Code Generation** — Rapid prototyping services
4. **Consulting** — AI integration strategy

**Key Insight:**
> "The people making money aren't using OpenClaw to replace themselves — they're using it to 10x their output."

---

## MCP (Model Context Protocol)

**From NetworkChuck:**

**What is MCP:**
Standardized way for AI models to discover and use tools.

**Benefits:**
- Universal tool interface
- No custom integration per tool
- Dynamic tool discovery

**Example MCP Tools:**
- File system access
- Database queries
- API integrations
- Browser control

**Security Testing:**
- **HexStrike** — AI MCP for hacking/CTF
- Automated vulnerability scanning
- AI-powered reconnaissance

---

## Common Pitfalls

### 1. Token Limits
> "Always checkpoint at 78%. New agent spawns automatically."

### 2. Tool Calling Failures
> "If kimi stops calling tools, check OpenClaw version. 2026.3.2 is known-good."

### 3. Context Pollution
- Long conversations degrade performance
- Use fresh sessions for new tasks
- Archive old sessions

### 4. Permission Issues
- Desktop control needs accessibility
- Browser needs JavaScript Apple Events
- Check TOOLS.md for specific requirements

---

## Advanced Techniques

### Heartbeat Automation

**Use for:**
- Periodic checks (email, calendar)
- Batch operations
- Background tasks

**vs Cron:**
- Heartbeat: Flexible timing, conversational context
- Cron: Precise scheduling, isolated execution

### Sub-Agent Orchestration

```bash
# Spawn isolated task agent
openclaw sessions spawn \
  --task "Analyze this codebase" \
  --model kimi-coding/k2p5 \
  --mode run
```

### ACP (Agent Coding Protocol)

**Use when:**
- Complex coding tasks
- Need persistent thread
- Long-running development

```bash
openclaw sessions spawn \
  --runtime acp \
  --agentId claude-code \
  --thread
```

---

## Prerequisites

**Required:**
- Terminal proficiency
- Understanding of APIs and automation
- Basic Python (for scripting)

**Helpful:**
- [agentic-workflows-course](agentic-workflows-course.md) — Nick Saraev's deep dive
- [claude-code-course](claude-code-course.md) — 4-hour comprehensive guide

---

## Key Quotes

> "Use the plan. Plan mode is your friend."

> "The more specific you are, the better the output."

> "Local models work for focused, component-level development."

> "If you don't have a plan, you're planning to fail."

---

## Sources

| Source | Duration | Words | Creator |
|--------|----------|-------|---------|
| openclaw-master-10hr | 10 hrs | 64,300 | Mani Kanasani |
| openclaw-6hour-course | 6 hrs | 61,900 | Julian Goldie |
| agentic-workflows-course | 5.7 hrs | 66,200 | Nick Saraev |
| claude-code-course | 4 hrs | 56,300 | Nick Saraev |
| openclaw-fixed-setup | 1h 4m | 8,500 | Greg Isenberg |
| openclaw-army-agents | 18 min | 3,500 | Alex Finn |
| n8n-tutorial-zero-to-hero | 3.5 hrs | 35,400 | freeCodeCamp |

**Total:** ~296,000 words of OpenClaw expertise

---

*Synthesized from 7 sources — the definitive OpenClaw mastery guide*
