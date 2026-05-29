#!/usr/bin/env python3
import json

# Load catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# Add C++ course
cpp_source = {
    "source_id": "cpp-course-beginner-advanced",
    "display_name": "C++ Programming Course - Beginner to Advanced",
    "author": "CodeBeauty (YouTube)",
    "type": "course",
    "length": {
        "words": 340477,
        "duration_minutes": 1867
    },
    "concepts_covered": 27,
    "domains": ["coding", "cpp"]
}

catalog['sources']['cpp-course-beginner-advanced'] = cpp_source
catalog['total_sources'] = 37

# Add to by_type
catalog['by_type']['courses'].append('cpp-course-beginner-advanced')

# Add to by_domain
catalog['by_domain']['coding'].append('cpp-course-beginner-advanced')
catalog['by_domain']['cpp'] = ['cpp-course-beginner-advanced']

# Save
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✅ C++ course added to catalog")
print(f"Total sources: {catalog['total_sources']}")
