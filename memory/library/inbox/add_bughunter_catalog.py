import json

# Read the current catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# New source entry
new_source = {
    "source_id": "bug-hunter-methodology",
    "display_name": "The Bug Hunter's Methodology - Full 2-Hour Training",
    "author": "Jason Haddix (Red Team Village)",
    "type": "video",
    "length": {
        "words": 12677,
        "duration_minutes": 113
    },
    "concepts_covered": 15,
    "domains": [
        "cybersecurity",
        "bug-bounty",
        "penetration-testing"
    ]
}

# Add to catalog
catalog["sources"]["bug-hunter-methodology"] = new_source
catalog["total_sources"] = 42

# Add to by_type
catalog["by_type"]["videos"].append("bug-hunter-methodology")

# Add to by_domain
for domain in ["cybersecurity", "bug-bounty", "penetration-testing"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("bug-hunter-methodology")

# Update last_updated
catalog["last_updated"] = "2026-03-23"

# Save back
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 42: The Bug Hunter's Methodology - Full 2-Hour Training")
print(f"✓ Total sources: {catalog['total_sources']}")
