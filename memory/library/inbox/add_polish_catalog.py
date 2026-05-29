import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "networkchuck-mitm-polish",
    "display_name": "how Hackers SNiFF (capture) network traffic // MiTM attack [Polish]",
    "author": "NetworkChuck",
    "type": "video",
    "length": {
        "words": 436,
        "duration_minutes": 19
    },
    "concepts_covered": 6,
    "domains": [
        "cybersecurity",
        "networking",
        "mitm"
    ],
    "language": "Polish (auto-generated)",
    "note": "Polish transcript - MiTM attacks, packet sniffing, network traffic capture"
}

catalog["sources"]["networkchuck-mitm-polish"] = new_source
catalog["total_sources"] = 57

catalog["by_type"]["videos"].append("networkchuck-mitm-polish")

for domain in ["cybersecurity", "networking", "mitm"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("networkchuck-mitm-polish")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 57: NetworkChuck MiTM attack [Polish]")
print(f"✓ Total sources: {catalog['total_sources']}")
print("✓ Language: Polish (auto-generated)")
