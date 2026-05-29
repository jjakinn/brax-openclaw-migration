import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "live-recon-snapchat",
    "display_name": "Live Recon on Snapchat with @ITSecurityGuard (amass, FFUF, SecurityTrails Demo)",
    "author": "NahamSec / ITSecurityGuard",
    "type": "video",
    "length": {
        "words": 12958,
        "duration_minutes": 101
    },
    "concepts_covered": 11,
    "domains": [
        "cybersecurity",
        "reconnaissance",
        "bug-bounty"
    ]
}

catalog["sources"]["live-recon-snapchat"] = new_source
catalog["total_sources"] = 44

catalog["by_type"]["videos"].append("live-recon-snapchat")

for domain in ["cybersecurity", "reconnaissance", "bug-bounty"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("live-recon-snapchat")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 44: Live Recon on Snapchat with @ITSecurityGuard")
print(f"✓ Total sources: {catalog['total_sources']}")
