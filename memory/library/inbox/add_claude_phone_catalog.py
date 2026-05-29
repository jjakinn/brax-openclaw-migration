import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "claude-phone-calls",
    "display_name": "FREE Phone Calls with Claude Code",
    "author": "NetworkChuck (YouTube)",
    "type": "video",
    "length": {
        "words": 3746,
        "duration_minutes": 19
    },
    "concepts_covered": 8,
    "domains": [
        "claude",
        "ai",
        "automation",
        "voice",
        "telephony"
    ]
}

catalog["sources"]["claude-phone-calls"] = new_source
catalog["total_sources"] = 72

catalog["by_type"]["videos"].append("claude-phone-calls")

for domain in ["claude", "ai", "automation", "voice", "telephony"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("claude-phone-calls")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 72: FREE Phone Calls with Claude Code")
print(f"✓ Total sources: {catalog['total_sources']}")
