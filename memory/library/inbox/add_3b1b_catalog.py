import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "3b1b-neural-network",
    "display_name": "But what is a neural network? | Deep learning chapter 1",
    "author": "3Blue1Brown (Grant Sanderson)",
    "type": "video",
    "length": {
        "words": 2869,
        "duration_minutes": 18
    },
    "concepts_covered": 8,
    "domains": [
        "machine-learning",
        "neural-networks",
        "mathematics"
    ]
}

catalog["sources"]["3b1b-neural-network"] = new_source
catalog["total_sources"] = 46

catalog["by_type"]["videos"].append("3b1b-neural-network")

for domain in ["machine-learning", "neural-networks", "mathematics"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("3b1b-neural-network")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 46: But what is a neural network? | Deep learning chapter 1")
print(f"✓ Total sources: {catalog['total_sources']}")
