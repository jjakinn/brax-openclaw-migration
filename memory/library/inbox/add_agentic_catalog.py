import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "agentic-workflows-course",
    "display_name": "AGENTIC WORKFLOWS 6 HOUR COURSE: Beginner to Pro (2026)",
    "author": "Nick Saraev (YouTube)",
    "type": "course",
    "length": {
        "words": 66276,
        "duration_minutes": 341
    },
    "concepts_covered": 22,
    "domains": [
        "ai",
        "automation",
        "workflows",
        "agents",
        "openclaw"
    ]
}

catalog["sources"]["agentic-workflows-course"] = new_source
catalog["total_sources"] = 70

catalog["by_type"]["courses"].append("agentic-workflows-course")

for domain in ["ai", "automation", "workflows", "agents", "openclaw"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("agentic-workflows-course")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 70: AGENTIC WORKFLOWS 6 HOUR COURSE")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 66,276")
print(f"✓ Chunks: 23")
