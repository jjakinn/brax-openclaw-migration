# Source: Free Unlimited Powerful Cloud LLM Tool (Ollama + Claude Code)
## URL: https://www.youtube.com/watch?v=N7CQdYaeUEE
## Ingested: 2026-03-25

---

## Overview
Tutorial on using Ollama with Claude Code to run local LLMs for free coding assistance, avoiding expensive cloud plan upgrades.

## Key Topics Covered

### 1. Ollama Installation
- Download from olama.com
- Install via terminal: `brew install ollama` (Mac)
- Verify: `ollama --version`
- List models: `ollama list`

### 2. Recommended Models for Claude Code

**Based on VRAM specs:**

| Model | Parameters | VRAM Required | Best For |
|-------|-----------|---------------|----------|
| Qwen 2.5 Coder | 3B | ~4GB | Lightweight coding |
| Qwen 2.5 Coder | 8B | 11GB | Balanced performance |
| Qwen 2.5 Coder | 14B | ~18GB | Better accuracy |
| Qwen 2.5 Coder | 32B | ~35GB | Highest accuracy |
| DeepSeek Coder | Various | Varies | Alternative option |
| Gemma 4 | 9B | ~10GB | Google model |

**Install command:**
```bash
ollama pull qwen2.5-coder:8b
```

### 3. Claude Code Configuration

**Launch with local model:**
```bash
claude --config
# Select from available Ollama models
```

**Switch models:**
```bash
claude --config
# Choose different installed model
```

### 4. Cloud Alternative: GLM-4.7

**Zhipu AI GLM-4.7 (Free Tier)**
- 250,000 input tokens/hour free
- Runs in cloud (not local)
- Better accuracy than local models
- Install: `ollama pull glm-4.7`

**Comparison:**
- Local models: Free, private, but lower accuracy
- GLM-4.7 cloud: Free tier, better accuracy, cloud-hosted
- Claude Opus 4.5: Best accuracy, paid

### 5. Best Practices for Local Models

**Storybook Component Development:**
- Break down UI into single components
- Perfect one component at a time
- Less context = better local model performance
- Install: `npx storybook@latest init`

**Tips for Better Results:**
1. Work on small, focused components
2. Use plan mode for complex tasks
3. Iterate and refine
4. Take screenshots for feedback
5. Be specific in prompts

### 6. Frontend Design Skill Integration

**Using with Claude Code:**
```
/plan
[Frontend Design Skill]
Redesign email template with cleaner look
Create terminal wireframe first
```

### 7. Model Accuracy Comparison

**Observed performance:**
- Local 8B models: Basic tasks, some inaccuracies
- Local 32B models: Better but high VRAM needs
- GLM-4.7 cloud: Good balance of free + accuracy
- Claude Opus 4.5: Best overall (paid)

## Commands Reference

```bash
# Install Ollama
brew install ollama

# Pull models
ollama pull qwen2.5-coder:8b
ollama pull qwen2.5-coder:14b
ollama pull gemma4:9b

# List installed
ollama list

# Launch Claude with local model
claude --config

# Check Ollama version
ollama --version
```

## Key Takeaways

1. **Local models work** for focused, component-level development
2. **Storybook approach** maximizes local model effectiveness
3. **GLM-4.7 free tier** offers good middle ground
4. **VRAM is the limiting factor** for local model size
5. **Accuracy trade-off** exists vs cloud models

## Prerequisites
- macOS/Linux/Windows with WSL
- Sufficient RAM/VRAM for chosen model
- Claude Code installed

## Related Sources
- OpenClaw course (Source 64)
- Claude Code courses (Sources 68, 70)
- MCP tutorial (Source 76)

---
**Word count:** ~2,200 words  
**Duration:** ~15 minutes  
**Source ID:** 78
