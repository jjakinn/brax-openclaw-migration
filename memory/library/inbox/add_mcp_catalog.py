import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "mcp-networkchuck",
    "display_name": "you need to learn MCP RIGHT NOW!! (Model Context Protocol)",
    "author": "NetworkChuck (YouTube)",
    "type": "video",
    "length": {
        "words": 6714,
        "duration_minutes": 38
    },
    "concepts_covered": 12,
    "domains": [
        "ai",
        "mcp",
        "model-context-protocol",
        "automation"
    ]
}

catalog["sources"]["mcp-networkchuck"] = new_source
catalog["total_sources"] = 76

catalog["by_type"]["videos"].append("mcp-networkchuck")

for domain in ["ai", "mcp", "model-context-protocol", "automation"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("mcp-networkchuck")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 76: you need to learn MCP RIGHT NOW!! (Model Context Protocol)")
print(f"✓ Total sources: {catalog['total_sources']}")
