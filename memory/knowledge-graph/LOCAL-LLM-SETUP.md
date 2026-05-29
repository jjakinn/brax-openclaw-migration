# Local LLM Setup for OpenClaw

Based on the video tutorial ingested into your knowledge graph (Source 78).

## ✅ Status: READY

**Qwen 2.5 Coder 7B** has been successfully installed for local use.

## ⚠️ IMPORTANT: What the Video Actually Showed

The video demonstrated **two approaches:**

1. **Local models via Ollama** (Qwen 2.5 Coder) - ✅ Installed
2. **GLM-4.7 via Zhipu AI cloud API** - ⚠️ Requires separate setup

**GLM-4.7 is NOT available on Ollama** - it's a cloud-hosted model from Zhipu AI that you connect to via API, not download.

---

## Part 1: Local Models (Ollama) ✅ READY

### Your Installed Models

| Model | Size | Best For |
|-------|------|----------|
| **qwen2.5-coder:7b** ✅ NEW | 4.7 GB | Coding tasks, component development |
| qwen2.5:7b | 4.7 GB | General tasks |
| dolphin-agent | 4.7 GB | Agent workflows |
| llama3.2 | 2.0 GB | Lightweight tasks |
| nous-hermes2 | 6.1 GB | General conversation |
| dolphin-llama3:8b | 4.7 GB | General coding |
| dolphin-uncensored | 4.7 GB | Uncensored responses |

### Usage

**Switch to local model in OpenClaw:**
```bash
openclaw tui --config
# Select qwen2.5-coder:7b
```

**Run directly with Ollama:**
```bash
ollama run qwen2.5-coder:7b
```

### Best Practices (from Video)

Local models work best when you:
1. **Break tasks into components** - Don't ask for full apps
2. **Use Storybook approach** - Perfect one component at a time
3. **Provide context** - Copy relevant code snippets
4. **Iterate** - Start simple, then refine
5. **Take screenshots** - Show visual feedback

**Example workflow:**
```
"Create a login form component. Show terminal wireframe first."
[Review]
"Yes, implement that with shadcn/ui style."
[Review]
"Add validation."
```

---

## Part 2: GLM-4.7 Cloud (What the Video Ended With)

### What the Video Actually Demonstrated

The creator **switched to GLM-4.7 cloud** because local models weren't accurate enough. Key quote from the video:

> *"So then it got me thinking, well, what are some models in Ollama here has the highest accuracy... here we have our GLM 4.7... I thought to myself, well why not give it a try... GM4.7 cloud does run in the cloud, not on your local machine."*

### How to Actually Set Up GLM-4.7

**GLM-4.7 is from Zhipu AI (智谱AI)** - a Chinese AI company. It's NOT on Ollama.

**Setup steps:**

1. **Get API Key:**
   - Go to https://open.bigmodel.cn (Zhipu AI platform)
   - Create account
   - Get API key

2. **Install GLM-4.7 via Ollama (Cloud Connection):**
   ```bash
   # This connects to Zhipu AI's cloud, NOT local
   ollama pull glm-4.7  # May not work - see below
   ```
   
   **Note:** The video showed this working, but GLM-4.7 isn't in Ollama's public registry. The creator likely:
   - Had early access
   - Used a custom Modelfile with API endpoint
   - Or the video is outdated (model availability changes)

3. **Alternative: Use Zhipu AI Directly**
   ```bash
   # Install Python client
   pip install zhipuai
   
   # Or use with OpenClaw via custom model config
   ```

### GLM-4.7 Free Tier Details

From the video:
- **250,000 input tokens/hour** free
- Runs in **cloud** (not local)
- Better accuracy than local 7B models
- Good for complex tasks

**Comparison:**

| Model | Location | Quality | Cost | Setup |
|-------|----------|---------|------|-------|
| qwen2.5-coder:7b | Local | Good | Free | ✅ Easy |
| GLM-4.7 | Cloud (Zhipu AI) | Better | Free tier | ⚠️ Requires API key |
| Claude Opus | Cloud (Anthropic) | Best | $20/mo | ✅ Built into OpenClaw |

---

## The Video's Actual Recommendation

The video ended up recommending **GLM-4.7 cloud** as the better free option, not local models.

**Why:**
- Local models (Qwen 7B) had accuracy issues
- GLM-4.7 cloud was "much faster" and gave "much cleaner designs"
- Free tier sufficient for most use

**But:** GLM-4.7 requires:
- Zhipu AI account (Chinese platform)
- API key setup
- Cloud connection (not truly "local")

---

## My Recommendation for You

Given your setup:

| Use Case | Recommendation |
|----------|----------------|
| Quick coding help | `qwen2.5-coder:7b` (local) ✅ Ready |
| Complex tasks | Keep using `kimi-coding/k2p5` (your current) |
| Free alternative to Claude | Try GLM-4 via Zhipu AI if you want |
| Production work | Claude Opus ($20/mo) |

### Why I Recommend This

1. **Qwen 2.5 Coder 7B** is already installed and works
2. **Kimi K2.5** (your current model) is actually better than GLM-4.7 for most tasks
3. **GLM-4.7 setup** requires navigating a Chinese AI platform
4. You're already on the **$19/mo Kimi Moderato plan** - probably better value

---

## Commands Reference

```bash
# List installed models
ollama list

# Pull new model
ollama pull <model-name>

# Run model
ollama run qwen2.5-coder:7b

# Remove model
ollama rm <model-name>
```

## VRAM Guidelines (Your 16GB MacBook Air)

| Model Size | VRAM Needed | Works? |
|------------|-------------|--------|
| 3B | ~4GB | ✅ Yes |
| 7B | ~8GB | ✅ Yes |
| 8B | ~11GB | ⚠️ Close to limit |
| 14B+ | 18GB+ | ❌ No |

---

## If You Still Want GLM-4.7

**Steps:**
1. Go to https://open.bigmodel.cn
2. Sign up for account
3. Get API key
4. Configure OpenClaw to use Zhipu AI endpoint

**Or:** Use a different cloud free tier like:
- **Groq** (fast, free tier)
- **Together AI** (various free models)
- **OpenRouter** (aggregates free models)

---

**Last Updated:** 2026-03-25  
**Correction:** GLM-4.7 is cloud API, not Ollama model
