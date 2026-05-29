import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "osint-full-course",
    "display_name": "Open-Source Intelligence (OSINT) in 5 Hours - Full Course - Learn OSINT!",
    "author": "The Cyber Mentor (Heath Adams)",
    "type": "course",
    "length": {
        "words": 45245,
        "duration_minutes": 269
    },
    "concepts_covered": 20,
    "domains": [
        "cybersecurity",
        "osint",
        "reconnaissance",
        "investigation"
    ]
}

catalog["sources"]["osint-full-course"] = new_source
catalog["total_sources"] = 61

catalog["by_type"]["courses"].append("osint-full-course")

for domain in ["cybersecurity", "osint", "reconnaissance", "investigation"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("osint-full-course")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 61: Open-Source Intelligence (OSINT) in 5 Hours - Full Course")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 45,245 (largest OSINT source)")
