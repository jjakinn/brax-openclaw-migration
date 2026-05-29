import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "dark-web-exposed",
    "display_name": "The Dark Web EXPOSED (FREE + Open-Source Tool)",
    "author": "NetworkChuck (YouTube)",
    "type": "video",
    "length": {
        "words": 3800,
        "duration_minutes": 20
    },
    "concepts_covered": 8,
    "domains": [
        "cybersecurity",
        "dark-web",
        "osint",
        "privacy"
    ]
}

catalog["sources"]["dark-web-exposed"] = new_source
catalog["total_sources"] = 73

catalog["by_type"]["videos"].append("dark-web-exposed")

for domain in ["cybersecurity", "dark-web", "osint", "privacy"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("dark-web-exposed")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 73: The Dark Web EXPOSED (FREE + Open-Source Tool)")
print(f"✓ Total sources: {catalog['total_sources']}")
