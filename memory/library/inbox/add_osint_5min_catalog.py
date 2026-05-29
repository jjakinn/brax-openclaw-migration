import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "osint-5min",
    "display_name": "Every OSINT Technique Explained in 5 Minutes",
    "author": "Mr Ethical Hacker (YouTube)",
    "type": "video",
    "length": {
        "words": 677,
        "duration_minutes": 4
    },
    "concepts_covered": 8,
    "domains": [
        "cybersecurity",
        "osint",
        "reconnaissance"
    ]
}

catalog["sources"]["osint-5min"] = new_source
catalog["total_sources"] = 62

catalog["by_type"]["videos"].append("osint-5min")

for domain in ["cybersecurity", "osint", "reconnaissance"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("osint-5min")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 62: Every OSINT Technique Explained in 5 Minutes")
print(f"✓ Total sources: {catalog['total_sources']}")
