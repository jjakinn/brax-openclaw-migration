import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "bug-hunter-app-analysis",
    "display_name": "The Bug Hunter's Methodology - Application Analysis",
    "author": "Jason Haddix (HackerOne)",
    "type": "video",
    "length": {
        "words": 7027,
        "duration_minutes": 47
    },
    "concepts_covered": 10,
    "domains": [
        "cybersecurity",
        "bug-bounty",
        "application-security"
    ]
}

catalog["sources"]["bug-hunter-app-analysis"] = new_source
catalog["total_sources"] = 43

catalog["by_type"]["videos"].append("bug-hunter-app-analysis")

for domain in ["cybersecurity", "bug-bounty", "application-security"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("bug-hunter-app-analysis")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 43: The Bug Hunter's Methodology - Application Analysis")
print(f"✓ Total sources: {catalog['total_sources']}")
