import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-making-money",
    "display_name": "Making $$$ with OpenClaw",
    "author": "Greg Isenberg (YouTube)",
    "type": "video",
    "length": {
        "words": 8005,
        "duration_minutes": 52
    },
    "concepts_covered": 10,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "business",
        "monetization"
    ]
}

catalog["sources"]["openclaw-making-money"] = new_source
catalog["total_sources"] = 67

catalog["by_type"]["videos"].append("openclaw-making-money")

for domain in ["openclaw", "ai", "automation", "business", "monetization"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-making-money")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 67: Making $$$ with OpenClaw")
print(f"✓ Total sources: {catalog['total_sources']}")
