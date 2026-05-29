# HEARTBEAT.md

## Automated Checks (Local Model - free)

When heartbeat triggers, run these checks using `ollama/llama3.2`:

1. **Token Usage** - Check all model usage; alert if any >70%
2. **Cache Stats** - Report hit rate, tokens saved
3. **Rate Limits** - Show free model quota remaining
4. **Active Tasks** - Are there paused checkpoints needing work?
5. **Cleanup** - Archive old cache entries (>24h)

Output format:
```
[HEARTBEAT] Token usage: X%
[HEARTBEAT] Cache hit rate: Y% (Z tokens saved)
[HEARTBEAT] Free model quotas: gemini:余, claude:余, llama3.3:余, mixtral:余
[HEARTBEAT] Paused tasks: N
```

If anything urgent (>80% tokens, zero free quota, high-priority paused task) → send alert message.
Otherwise → HEARTBEAT_OK.
