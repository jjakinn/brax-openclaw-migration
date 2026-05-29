import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "osint-beginners",
    "display_name": "OSINT for Beginners: Find Everything About Anyone!",
    "author": "Loi Liang Yang (YouTube)",
    "type": "video",
    "length": {
        "words": 2416,
        "duration_minutes": 14
    },
    "concepts_covered": 8,
    "domains": [
        "cybersecurity",
        "osint",
        "reconnaissance"
    ]
}

catalog["sources"]["osint-beginners"] = new_source
catalog["total_sources"] = 60

catalog["by_type"]["videos"].append("osint-beginners")

for domain in ["cybersecurity", "osint", "reconnaissance"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("osint-beginners")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 60: OSINT for Beginners: Find Everything About Anyone!")
print(f"✓ Total sources: {catalog['total_sources']}")
