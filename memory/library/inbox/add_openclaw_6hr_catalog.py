import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-6hour-course",
    "display_name": "OpenClaw AI FULL 6 Hour Course",
    "author": "Julian Goldie SEO (YouTube)",
    "type": "course",
    "length": {
        "words": 61905,
        "duration_minutes": 359
    },
    "concepts_covered": 22,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "workflow",
        "seo"
    ]
}

catalog["sources"]["openclaw-6hour-course"] = new_source
catalog["total_sources"] = 66

catalog["by_type"]["courses"].append("openclaw-6hour-course")

for domain in ["openclaw", "ai", "automation", "workflow", "seo"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-6hour-course")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 66: OpenClaw AI FULL 6 Hour Course")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 61,905")
print(f"✓ Chunks: 21")
