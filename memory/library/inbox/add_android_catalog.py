import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "android-hacking-workshop",
    "display_name": "Android Hacking Workshop by @B3nacSec",
    "author": "B3nacSec (HackerOne)",
    "type": "video",
    "length": {
        "words": 1814,
        "duration_minutes": 18
    },
    "concepts_covered": 7,
    "domains": [
        "cybersecurity",
        "mobile-security",
        "android"
    ]
}

catalog["sources"]["android-hacking-workshop"] = new_source
catalog["total_sources"] = 56

catalog["by_type"]["videos"].append("android-hacking-workshop")

for domain in ["cybersecurity", "mobile-security", "android"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("android-hacking-workshop")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 56: Android Hacking Workshop by @B3nacSec")
print(f"✓ Total sources: {catalog['total_sources']}")
