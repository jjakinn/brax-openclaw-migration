# Smart Cache & Router Skill

## Purpose
Minimize token costs by:
1. Routing queries to the cheapest appropriate model
2. Caching frequent queries to avoid re-computation
3. Intelligent fallback when rate limits hit

## How It Works

### Model Routing Decision Tree
```
if query requires reasoning:
  if kimi-coding/k2p5 available and tokens < 100k: use kimi (paid, high quality)
  else: check free cloud models in order:
    - claude-3-haiku:free (complex)
    - gemini-2.5-flash-lite:free (general)
    - llama-3.3-70b:free (heavy)
    - mixtral-8x7b:free (heavy)
    - llama3.2 (local) as fallback
else:
  use ollama/llama3.2 (free, no rate limit)
```

### Cache Check Flow
Before any model call:
1. Hash: `sha256(query + model + params)`
2. Look up in `memory/cache/query-responses.jsonl`
3. If found and age < TTL (24h) → return cached response
4. If not found → proceed to model call, then cache result

### Rate Limit Handling
- Maintain `memory/cache/rate-limits.json` tracking:
  ```json
  {
    "openrouter/google/gemini-2.5-flash-lite:free": {
      "limit": 1000,
      "used": 847,
      "reset": "2026-03-24T12:00:00Z"
    }
  }
  ```
- If model at >90% of limit → auto-route to alternative
- Only use paid models (kimi) as last resort

## Integration
Agent automatically uses this skill for all model calls.
No explicit invocation needed — it's transparent.

## Expected Savings
- 30-50% from cache hits on repetitive work
- 80%+ from preferring free/local models
- Unlimited effective capacity via rotation

## Requirements
- Free models configured in `openclaw.json` (see openclaw-free-models skill)
- Cache directory writable: `memory/cache/`
- Agent uses `ollama/llama3.2` for local fallback