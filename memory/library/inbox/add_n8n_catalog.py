import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "n8n-tutorial",
    "display_name": "n8n Tutorial – Zero to Hero Course",
    "author": "freeCodeCamp.org",
    "type": "course",
    "length": {
        "words": 35453,
        "duration_minutes": 215
    },
    "concepts_covered": 18,
    "domains": [
        "automation",
        "workflows",
        "n8n",
        "no-code"
    ]
}

catalog["sources"]["n8n-tutorial"] = new_source
catalog["total_sources"] = 71

catalog["by_type"]["courses"].append("n8n-tutorial")

for domain in ["automation", "workflows", "n8n", "no-code"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("n8n-tutorial")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 71: n8n Tutorial – Zero to Hero Course")
print(f"✓ Total sources: {catalog['total_sources']}")
print(f"✓ Words: 35,453")
print(f"✓ Chunks: 12")
