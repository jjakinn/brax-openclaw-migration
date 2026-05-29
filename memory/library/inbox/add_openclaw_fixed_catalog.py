import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-fixed-setup",
    "display_name": "I fixed OpenClaw so it actually works (full setup)",
    "author": "Greg Isenberg (YouTube)",
    "type": "video",
    "length": {
        "words": 8595,
        "duration_minutes": 64
    },
    "concepts_covered": 10,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "setup",
        "troubleshooting"
    ]
}

catalog["sources"]["openclaw-fixed-setup"] = new_source
catalog["total_sources"] = 69

catalog["by_type"]["videos"].append("openclaw-fixed-setup")

for domain in ["openclaw", "ai", "automation", "setup", "troubleshooting"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-fixed-setup")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 69: I fixed OpenClaw so it actually works (full setup)")
print(f"✓ Total sources: {catalog['total_sources']}")
