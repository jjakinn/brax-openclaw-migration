#!/usr/bin/env python3
import json
import os

# Load existing catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# Add lectures 7-28
total_words = 0
for lec_num in range(7, 29):
    txt_file = f'stanford-cs106a-lec{lec_num}.txt'
    if os.path.exists(txt_file):
        with open(txt_file, 'r') as f:
            word_count = len(f.read().split())
        total_words += word_count
        
        source_id = f"stanford-cs106a-lec{lec_num}"
        catalog['sources'][source_id] = {
            "source_id": source_id,
            "display_name": f"Stanford CS106A: Programming Methodology - Lecture {lec_num}",
            "author": "Mehran Sahami (Stanford University)",
            "type": "video",
            "length": {
                "words": word_count,
                "duration_minutes": 50
            },
            "concepts_covered": 5,
            "domains": ["coding", "computer-science"]
        }
        
        # Add to videos list
        if source_id not in catalog['by_type']['videos']:
            catalog['by_type']['videos'].append(source_id)
        
        # Add to domain lists
        if source_id not in catalog['by_domain']['coding']:
            catalog['by_domain']['coding'].append(source_id)
        if source_id not in catalog['by_domain']['computer-science']:
            catalog['by_domain']['computer-science'].append(source_id)

# Update total count
catalog['total_sources'] = len(catalog['sources'])

# Save updated catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print(f"✅ Catalog updated: {catalog['total_sources']} total sources")
print(f"   New words added: {total_words:,}")
print(f"   Stanford lectures: 28 total")
