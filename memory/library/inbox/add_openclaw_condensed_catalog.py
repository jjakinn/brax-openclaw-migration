import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-100hrs-condensed",
    "display_name": "100 hours of OpenClaw lessons in 35 minutes",
    "author": "Alex Finn (YouTube)",
    "type": "video",
    "length": {
        "words": 6748,
        "duration_minutes": 35
    },
    "concepts_covered": 15,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "workflow"
    ]
}

catalog["sources"]["openclaw-100hrs-condensed"] = new_source
catalog["total_sources"] = 65

catalog["by_type"]["videos"].append("openclaw-100hrs-condensed")

for domain in ["openclaw", "ai", "automation", "workflow"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-100hrs-condensed")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 65: 100 hours of OpenClaw lessons in 35 minutes")
print(f"✓ Total sources: {catalog['total_sources']}")
