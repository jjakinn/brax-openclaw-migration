# Memory Chunking Protocol v3.1

## Semantic Chunking Strategy

Split content by **conceptual boundaries**, not character count.

### Chunk Types

| Type | Description | Max Size | Example |
|------|-------------|----------|---------|
| `concept` | Single idea/definition | 500 chars | "Neural networks are..." |
| `procedure` | Step-by-step process | 1000 chars | Build commands, workflows |
| `decision` | Choice + rationale | 800 chars | "Used X because Y..." |
| `reference` | Linkable fact | 400 chars | API endpoint, config value |
| `synthesis` | Multi-source insight | 2000 chars | Cross-referenced analysis |

### Metadata Tags (Auto-Generated)

Every chunk gets:
```json
{
  "chunk_id": "uuid-v4",
  "type": "concept|procedure|decision|reference|synthesis",
  "source": "filename.md",
  "created": "2026-04-01T14:55:00Z",
  "domains": ["coding", "security"],
  "concepts": ["neural-network", "backpropagation"],
  "confidence": 0.95,
  "access_count": 0,
  "last_accessed": null
}
```

### Cross-Linking Rules

1. **Concept mentions** → Link to canonical definition chunk
2. **Procedures** → Link to prerequisite procedures
3. **Decisions** → Link to alternatives considered
4. **Synthesis** → Link to all source chunks

### Auto-Chunking Command

```bash
# Chunk a new source file
python3 memory/knowledge-graph/tools/chunker.py \
  --input library/inbox/new-video.md \
  --type concept \
  --domains coding,security \
  --output memory/knowledge-graph/corpus/by-source/
```

### Manual Chunk Markers

In any `.md` file, use markers for fine-grained chunking:

```markdown
<!-- chunk:start type=concept id=backprop-calc domains=math,ml -->
Backpropagation uses the chain rule to compute gradients...
<!-- chunk:end -->

<!-- chunk:start type=procedure id=flask-setup domains=coding -->
1. pip install flask
2. Create app.py...
<!-- chunk:end -->
```

## Chunk Index

All chunks auto-register in:
`memory/knowledge-graph/index/chunk-registry.json`

Format:
```json
{
  "chunks": [
    {
      "id": "uuid",
      "file": "corpus/by-source/cs50.md",
      "byte_start": 15234,
      "byte_end": 15890,
      "metadata": {...}
    }
  ]
}
```

## Retrieval Enhancement

When searching:
1. Match query against chunk metadata
2. Boost by `access_count` (popular = relevant)
3. Prioritize `type=decision` for "how to" queries
4. Prioritize `type=reference` for "what is" queries
