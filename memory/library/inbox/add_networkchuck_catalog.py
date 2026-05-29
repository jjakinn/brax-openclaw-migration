import json

# Read the current catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# New source entry
new_source = {
    "source_id": "attacking-ai-jason-haddix",
    "display_name": "Attacking AI Version 1.1 w/ Jason Haddix",
    "author": "Antisyphon Training / Jason Haddix",
    "type": "video",
    "length": {
        "words": 10776,
        "duration_minutes": 61
    },
    "concepts_covered": 12,
    "domains": [
        "cybersecurity",
        "ai",
        "prompt-injection"
    ]
}

# Add to catalog
catalog["sources"]["attacking-ai-jason-haddix"] = new_source
catalog["total_sources"] = 41

# Add to by_type
catalog["by_type"]["videos"].append("attacking-ai-jason-haddix")

# Add to by_domain
for domain in ["cybersecurity", "ai", "prompt-injection"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("attacking-ai-jason-haddix")

# Update last_updated
catalog["last_updated"] = "2026-03-23"

# Save back
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 41: Attacking AI Version 1.1 w/ Jason Haddix")
print(f"✓ Total sources: {catalog['total_sources']}")
