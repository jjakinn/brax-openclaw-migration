import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "claude-code-course",
    "display_name": "CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026)",
    "author": "Nick Saraev (YouTube)",
    "type": "course",
    "length": {
        "words": 56345,
        "duration_minutes": 250
    },
    "concepts_covered": 20,
    "domains": [
        "ai",
        "coding",
        "automation",
        "business",
        "claude"
    ]
}

catalog["sources"]["claude-code-course"] = new_source
catalog["total_sources"] = 68

catalog["by_type"]["courses"].append("claude-code-course")

for domain in ["ai", "coding", "automation", "business", "claude"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("claude-code-course")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 68: CLAUDE CODE FULL COURSE 4 HOURS")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 56,345")
print(f"✓ Chunks: 19")
