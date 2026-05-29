#!/usr/bin/env python3
import json

# Load catalog
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'r') as f:
    catalog = json.load(f)

# Add Generative AI course
genai_source = {
    "source_id": "generative-ai-full-course",
    "display_name": "Generative AI Full Course – Gemini Pro, OpenAI, Llama, Langchain, Pinecone, Vector Databases",
    "author": "FreeCodeCamp / YouTube Creator",
    "type": "course",
    "length": {
        "words": 292238,
        "duration_minutes": 1818
    },
    "concepts_covered": 19,
    "domains": ["ai", "machine-learning", "generative-ai"]
}

catalog['sources']['generative-ai-full-course'] = genai_source
catalog['total_sources'] = 38

# Add to by_type
catalog['by_type']['courses'].append('generative-ai-full-course')

# Add to by_domain
catalog['by_domain']['ai'] = ['generative-ai-full-course']
catalog['by_domain']['machine-learning'] = ['generative-ai-full-course']
catalog['by_domain']['generative-ai'] = ['generative-ai-full-course']

# Save
with open('/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/indexes/sources-catalog.json', 'w') as f:
    json.dump(catalog, f, indent=2)

print("✅ Generative AI course added to catalog")
print(f"Total sources: {catalog['total_sources']}")
print(f"New words: 292,238")
