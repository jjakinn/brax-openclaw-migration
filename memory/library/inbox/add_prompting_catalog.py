import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "ai-prompting-secrets",
    "display_name": "You SUCK at Prompting AI (Here's the secret)",
    "author": "NetworkChuck (YouTube)",
    "type": "video",
    "length": {
        "words": 4505,
        "duration_minutes": 23
    },
    "concepts_covered": 10,
    "domains": [
        "ai",
        "prompting",
        "prompt-engineering",
        "llm"
    ]
}

catalog["sources"]["ai-prompting-secrets"] = new_source
catalog["total_sources"] = 74

catalog["by_type"]["videos"].append("ai-prompting-secrets")

for domain in ["ai", "prompting", "prompt-engineering", "llm"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("ai-prompting-secrets")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 74: You SUCK at Prompting AI (Here's the secret)")
print(f"✓ Total sources: {catalog['total_sources']}")
