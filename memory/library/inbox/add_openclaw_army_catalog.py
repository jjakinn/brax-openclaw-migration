import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-army",
    "display_name": "How to build an army of OpenClaw agents",
    "author": "Alex Finn (YouTube)",
    "type": "video",
    "length": {
        "words": 3561,
        "duration_minutes": 18
    },
    "concepts_covered": 8,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "workflow"
    ]
}

catalog["sources"]["openclaw-army"] = new_source
catalog["total_sources"] = 63

catalog["by_type"]["videos"].append("openclaw-army")

for domain in ["openclaw", "ai", "automation", "workflow"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-army")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 63: How to build an army of OpenClaw agents")
print(f"✓ Total sources: {catalog['total_sources']}")
