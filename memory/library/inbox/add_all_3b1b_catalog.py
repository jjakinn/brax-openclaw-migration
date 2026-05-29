import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_sources = [
    {
        "source_id": "3b1b-gradient-descent",
        "display_name": "Gradient descent, how neural networks learn | Deep Learning Chapter 2",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 3171, "duration_minutes": 21},
        "concepts_covered": 7,
        "domains": ["machine-learning", "neural-networks", "mathematics"]
    },
    {
        "source_id": "3b1b-backprop-intuition",
        "display_name": "Backpropagation, intuitively | Deep Learning Chapter 3",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 1936, "duration_minutes": 13},
        "concepts_covered": 6,
        "domains": ["machine-learning", "neural-networks", "mathematics"]
    },
    {
        "source_id": "3b1b-backprop-calculus",
        "display_name": "Backpropagation calculus | Deep Learning Chapter 4",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 1632, "duration_minutes": 11},
        "concepts_covered": 8,
        "domains": ["machine-learning", "neural-networks", "mathematics"]
    },
    {
        "source_id": "3b1b-llm-brief",
        "display_name": "Large Language Models explained briefly",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 1113, "duration_minutes": 6},
        "concepts_covered": 5,
        "domains": ["machine-learning", "llm", "ai"]
    },
    {
        "source_id": "3b1b-transformers",
        "display_name": "Transformers, the tech behind LLMs | Deep Learning Chapter 5",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 4434, "duration_minutes": 26},
        "concepts_covered": 9,
        "domains": ["machine-learning", "transformers", "llm", "ai"]
    },
    {
        "source_id": "3b1b-attention",
        "display_name": "Attention in transformers, step-by-step | Deep Learning Chapter 6",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 4215, "duration_minutes": 24},
        "concepts_covered": 8,
        "domains": ["machine-learning", "transformers", "attention", "ai"]
    },
    {
        "source_id": "3b1b-llm-facts",
        "display_name": "How might LLMs store facts | Deep Learning Chapter 7",
        "author": "3Blue1Brown (Grant Sanderson)",
        "type": "video",
        "length": {"words": 4089, "duration_minutes": 15},
        "concepts_covered": 7,
        "domains": ["machine-learning", "llm", "ai"]
    },
    {
        "source_id": "3b1b-ai-images",
        "display_name": "But how do AI images and videos actually work? | Guest video by Welch Labs",
        "author": "Welch Labs (3Blue1Brown series)",
        "type": "video",
        "length": {"words": 6497, "duration_minutes": 22},
        "concepts_covered": 8,
        "domains": ["machine-learning", "generative-ai", "diffusion-models", "ai"]
    }
]

for source in new_sources:
    catalog["sources"][source["source_id"]] = source
    catalog["by_type"]["videos"].append(source["source_id"])
    for domain in source["domains"]:
        if domain not in catalog["by_domain"]:
            catalog["by_domain"][domain] = []
        catalog["by_domain"][domain].append(source["source_id"])
    print(f"✓ Added: {source['display_name'][:60]}...")

catalog["total_sources"] = 54
catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print(f"\n✓ Total sources: {catalog['total_sources']}")
print(f"✓ Added 8 new 3Blue1Brown videos")
