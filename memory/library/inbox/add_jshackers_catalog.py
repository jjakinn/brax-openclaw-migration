import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "hacker101-javascript",
    "display_name": "Hacker101 - JavaScript for Hackers",
    "author": "@STOKfredrik (HackerOne)",
    "type": "video",
    "length": {
        "words": 3924,
        "duration_minutes": 24
    },
    "concepts_covered": 8,
    "domains": [
        "cybersecurity",
        "javascript",
        "web-security"
    ]
}

catalog["sources"]["hacker101-javascript"] = new_source
catalog["total_sources"] = 45

catalog["by_type"]["videos"].append("hacker101-javascript")

for domain in ["cybersecurity", "javascript", "web-security"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("hacker101-javascript")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 45: Hacker101 - JavaScript for Hackers")
print(f"✓ Total sources: {catalog['total_sources']}")
