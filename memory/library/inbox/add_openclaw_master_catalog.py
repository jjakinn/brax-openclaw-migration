import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "openclaw-master-course",
    "display_name": "Master OpenClaw in 10 Hours [I Created 5 AI Employees]",
    "author": "Mani Kanasani (YouTube)",
    "type": "course",
    "length": {
        "words": 64333,
        "duration_minutes": 603
    },
    "concepts_covered": 25,
    "domains": [
        "openclaw",
        "ai",
        "automation",
        "workflow",
        "multi-agent"
    ]
}

catalog["sources"]["openclaw-master-course"] = new_source
catalog["total_sources"] = 64

catalog["by_type"]["courses"].append("openclaw-master-course")

for domain in ["openclaw", "ai", "automation", "workflow", "multi-agent"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("openclaw-master-course")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 64: Master OpenClaw in 10 Hours")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 64,333 (LARGEST source in catalog!)")
print(f"✓ Chunks: 22")
