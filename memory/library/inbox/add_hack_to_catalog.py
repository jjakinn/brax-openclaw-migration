#!/usr/bin/env python3
import json

# Load catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# Add OpenClaw hacking video
hack_source = {
    "source_id": "openclaw-hacking-video",
    "display_name": "I Built an AI Agent That Hacks for Me | OpenClaw + Kali Linux",
    "author": "YouTube Creator",
    "type": "video",
    "length": {
        "words": 7720,
        "duration_minutes": 41
    },
    "concepts_covered": 7,
    "domains": ["cybersecurity", "ai", "openclaw"]
}

catalog['sources']['openclaw-hacking-video'] = hack_source
catalog['total_sources'] = 39

# Add to by_type
catalog['by_type']['videos'].append('openclaw-hacking-video')

# Add to by_domain
catalog['by_domain']['cybersecurity'] = ['openclaw-hacking-video']
if 'openclaw' not in catalog['by_domain']:
    catalog['by_domain']['openclaw'] = ['openclaw-hacking-video']
else:
    catalog['by_domain']['openclaw'].append('openclaw-hacking-video')

# Save
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✅ OpenClaw hacking video added to catalog")
print(f"Total sources: {catalog['total_sources']}")
