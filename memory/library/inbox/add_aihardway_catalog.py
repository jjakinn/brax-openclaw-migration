import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "ai-hard-way",
    "display_name": "You've Been Using AI the Hard Way (Use This Instead)",
    "author": "NetworkChuck (YouTube)",
    "type": "video",
    "length": {
        "words": 6408,
        "duration_minutes": 33
    },
    "concepts_covered": 10,
    "domains": [
        "ai",
        "automation",
        "workflows",
        "productivity"
    ]
}

catalog["sources"]["ai-hard-way"] = new_source
catalog["total_sources"] = 75

catalog["by_type"]["videos"].append("ai-hard-way")

for domain in ["ai", "automation", "workflows", "productivity"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("ai-hard-way")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 75: You've Been Using AI the Hard Way (Use This Instead)")
print(f"✓ Total sources: {catalog['total_sources']}")
