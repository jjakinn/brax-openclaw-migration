#!/usr/bin/env python3
import json

# Load catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# Add AI hacker beginner video
hacker_source = {
    "source_id": "ai-hacker-beginner",
    "display_name": "become an AI HACKER (it's easier than you think)",
    "author": "YouTube Creator",
    "type": "video",
    "length": {
        "words": 3441,
        "duration_minutes": 17
    },
    "concepts_covered": 4,
    "domains": ["cybersecurity", "ai"]
}

catalog['sources']['ai-hacker-beginner'] = hacker_source
catalog['total_sources'] = 40

# Add to by_type
catalog['by_type']['videos'].append('ai-hacker-beginner')

# Add to by_domain
catalog['by_domain']['cybersecurity'].append('ai-hacker-beginner')

# Save
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✅ AI hacker beginner video added to catalog")
print(f"Total sources: {catalog['total_sources']}")
