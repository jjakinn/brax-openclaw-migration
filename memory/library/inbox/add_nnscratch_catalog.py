import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "neural-network-scratch",
    "display_name": "I Built a Neural Network from Scratch",
    "author": "Green Code (YouTube)",
    "type": "video",
    "length": {
        "words": 1601,
        "duration_minutes": 9
    },
    "concepts_covered": 6,
    "domains": [
        "machine-learning",
        "neural-networks",
        "coding"
    ]
}

catalog["sources"]["neural-network-scratch"] = new_source
catalog["total_sources"] = 55

catalog["by_type"]["videos"].append("neural-network-scratch")

for domain in ["machine-learning", "neural-networks", "coding"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("neural-network-scratch")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 55: I Built a Neural Network from Scratch")
print(f"✓ Total sources: {catalog['total_sources']}")
