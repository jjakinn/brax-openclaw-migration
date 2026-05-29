# Your Ollama Cloud Setup

Based on what you're seeing in the Ollama app:

## Cloud Models Available (via Ollama App UI)

| Model | Type | Notes |
|-------|------|-------|
| **GLM-4.7** | Cloud (Zhipu AI) | 250K tokens/hour free tier |
| **Claude Code 470b-cloud** | Cloud (Anthropic via Ollama) | Larger model, cloud-hosted |

These appear in the **Ollama app's GUI** under a "Cloud" or "Remote" section - they're NOT downloaded locally (that's why `ollama list` doesn't show them).

## How It Works

The Ollama app acts as a **proxy/bridge**:
- You chat through the Ollama app UI
- It forwards to cloud APIs (Zhipu AI, Anthropic, etc.)
- Responses come back through Ollama interface
- **You don't need separate API keys** - Ollama handles authentication

## What You Actually Have

### Local Models (downloaded, run on your Mac):
```
qwen2.5-coder:7b      ✅ 4.7 GB
qwen2.5:7b            ✅ 4.7 GB
dolphin-agent         ✅ 4.7 GB
llama3.2              ✅ 2.0 GB
nous-hermes2          ✅ 6.1 GB
dolphin-uncensored    ✅ 4.7 GB
dolphin-llama3:8b     ✅ 4.7 GB
```

### Cloud Models (via Ollama app, not downloaded):
```
GLM-4.7               ☁️ Cloud (Zhipu AI)
Claude Code 470b      ☁️ Cloud (Anthropic)
```

## Using Cloud Models in OpenClaw

To use GLM-4.7 or Claude Code 470b-cloud with OpenClaw (not just the Ollama app):

### Option 1: Ollama as Proxy
```bash
# Check if Ollama exposes cloud models via API
curl http://localhost:11434/api/tags
```

If cloud models appear there, you can configure OpenClaw to use them.

### Option 2: Configure OpenClaw Directly
Edit `~/.openclaw/config.json`:

```json
{
  "models": {
    "glm-4.7": {
      "provider": "ollama",
      "model": "glm-4.7",
      "endpoint": "http://localhost:11434"
    },
    "claude-code-470b": {
      "provider": "ollama",
      "model": "claude-code:470b-cloud",
      "endpoint": "http://localhost:11434"
    }
  }
}
```

### Option 3: Use Ollama CLI with Cloud Models
Try:
```bash
# See if cloud models are available via CLI
ollama run glm-4.7

# Or
ollama run claude-code:470b-cloud
```

## Comparison

| Feature | Local Models | Cloud Models via Ollama |
|---------|--------------|------------------------|
| **Runs on** | Your Mac | Cloud (Zhipu AI, Anthropic) |
| **Internet needed** | No | Yes |
| **Cost** | Free | Free tier (250K tokens/hr) |
| **Privacy** | 100% local | Sent to cloud |
| **Speed** | Depends on Mac | Fast (cloud GPUs) |
| **Accuracy** | Good | Better |

## Quick Test

In your Ollama app, try asking GLM-4.7:
> "Write a Python function to calculate fibonacci numbers"

Then try the same with your local `qwen2.5-coder:7b` and compare.

---

**Bottom line:** You have both! Local models for privacy/offline work, cloud models via Ollama app for better accuracy when online.

Want me to help configure OpenClaw to use the cloud models through Ollama?
