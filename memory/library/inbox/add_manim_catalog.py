import json

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

new_source = {
    "source_id": "3b1b-manim-demo",
    "display_name": "How I animate 3Blue1Brown | A Manim demo with Ben Sparks",
    "author": "3Blue1Brown (Grant Sanderson) with Ben Sparks",
    "type": "video",
    "length": {
        "words": 11129,
        "duration_minutes": 53
    },
    "concepts_covered": 10,
    "domains": [
        "animation",
        "python",
        "manim",
        "mathematics"
    ]
}

catalog["sources"]["3b1b-manim-demo"] = new_source
catalog["total_sources"] = 58

catalog["by_type"]["videos"].append("3b1b-manim-demo")

for domain in ["animation", "python", "manim", "mathematics"]:
    if domain not in catalog["by_domain"]:
        catalog["by_domain"][domain] = []
    catalog["by_domain"][domain].append("3b1b-manim-demo")

catalog["last_updated"] = "2026-03-23"

with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✓ Added source 58: How I animate 3Blue1Brown | A Manim demo")
print(f"✓ Total sources: {catalog['total_sources']}")
