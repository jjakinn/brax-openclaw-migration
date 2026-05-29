# Cache System

## Purpose
Minimize token usage by caching frequent queries and responses.

## Structure
```
memory/cache/
├── query-responses.jsonl    # Query hash → {response, timestamp, model, tokens}
├── embeddings/             # Cached embeddings for knowledge base chunks
│   ├── by-source/
│   └── index.json
├── model-responses.jsonl   # Raw model response cache (exact prompt match)
└── stats.json              # Hit rates, savings

## TTL
- Query responses: 24 hours
- Embeddings: 7 days (unless source updates)
- Model responses: 1 hour (prompts change frequently)

## Usage
Before calling any model:
1. Compute hash of query/prompt
2. Check cache for recent entry
3. If hit and TTL valid → return cached response
4. If miss → call model, then cache result

## Expected Savings
30-50% reduction in token costs for repetitive tasks.