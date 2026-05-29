import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "manual-hacking-guide",
    "display_name": "Manual Hacking FULL GUIDE | Bug Bounty Explained",
    "author": "JakSec (YouTube)",
    "type": "video",
    "length": {
        "words": 13734,
        "duration_minutes": 86
    },
    "concepts_covered": 12,
    "domains": [
        "cybersecurity",
        "bug-bounty",
        "manual-testing"
    ]
}

catalog["sources"]["manual-hacking-guide"] = new_source
catalog["total_sources"] = 59

catalog["by_type"]["videos"].append("manual-hacking-guide")

for domain in ["cybersecurity", "bug-bounty", "manual-testing"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("manual-hacking-guide")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 59: Manual Hacking FULL GUIDE | Bug Bounty Explained")
print(f"✓ Total sources: {catalog['total_sources']}")
