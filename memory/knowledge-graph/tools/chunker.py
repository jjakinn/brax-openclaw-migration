#!/usr/bin/env python3
"""
Semantic Chunker
Chunks content by conceptual boundaries with metadata
"""

import json
import re
import hashlib
from pathlib import Path
from datetime import datetime

CHUNK_REGISTRY = Path("/Users/Jakin/.openclaw/workspace/memory/knowledge-graph/index/chunk-registry.json")

def generate_chunk_id(content, source):
    """Generate unique ID for chunk"""
    data = f"{source}:{content[:100]}"
    return hashlib.md5(data.encode()).hexdigest()[:12]

def detect_chunk_type(text):
    """Auto-detect chunk type from content"""
    text_lower = text.lower()
    
    # Check for procedures
    if re.search(r'^(\d+\.|\*|\-)\s+\w+', text, re.MULTILINE):
        if any(word in text_lower for word in ['step', 'command', 'run', 'install', 'build']):
            return 'procedure'
    
    # Check for decisions
    if any(phrase in text_lower for phrase in ['decided', 'chose', 'because', 'rationale', 'reason']):
        return 'decision'
    
    # Check for references
    if re.search(r'`[^`]+`|\b\w+:\/\/|\b\d+\.\d+\.\d+\.\d+', text):
        if len(text) < 500:
            return 'reference'
    
    # Default to concept
    return 'concept'

def extract_concepts(text):
    """Extract key concepts from text"""
    # Simple keyword extraction — could be enhanced with NLP
    words = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
    return list(set(words))[:5]  # Top 5 unique capitalized phrases

def chunk_content(content, source_file, domains=None, manual_markers=True):
    """
    Chunk content intelligently
    
    Args:
        content: Raw markdown content
        source_file: Source filename
        domains: List of domain tags
        manual_markers: Respect <!-- chunk:start --> markers
    """
    chunks = []
    
    if manual_markers and '<!-- chunk:' in content:
        # Parse manual markers
        pattern = r'<!-- chunk:start(.*?)-->(.*?)<!-- chunk:end -->'
        matches = re.findall(pattern, content, re.DOTALL)
        
        for attrs, text in matches:
            # Parse attributes
            attr_dict = {}
            for match in re.findall(r'(\w+)=(\S+)', attrs):
                attr_dict[match[0]] = match[1]
            
            chunk = {
                'id': attr_dict.get('id', generate_chunk_id(text, source_file)),
                'type': attr_dict.get('type', detect_chunk_type(text)),
                'source': str(source_file),
                'content': text.strip(),
                'created': datetime.now().isoformat(),
                'domains': attr_dict.get('domains', '').split(',') if 'domains' in attr_dict else (domains or []),
                'concepts': extract_concepts(text),
                'confidence': 1.0 if 'id' in attr_dict else 0.8,
                'access_count': 0,
                'last_accessed': None,
                'priority': attr_dict.get('priority', 'P2')
            }
            chunks.append(chunk)
    else:
        # Auto-chunk by headers
        sections = re.split(r'\n(?=#+\s)', content)
        
        for section in sections:
            if not section.strip():
                continue
                
            chunk = {
                'id': generate_chunk_id(section, source_file),
                'type': detect_chunk_type(section),
                'source': str(source_file),
                'content': section.strip(),
                'created': datetime.now().isoformat(),
                'domains': domains or [],
                'concepts': extract_concepts(section),
                'confidence': 0.7,
                'access_count': 0,
                'last_accessed': None,
                'priority': 'P2'
            }
            chunks.append(chunk)
    
    return chunks

def register_chunks(chunks):
    """Register chunks in index"""
    if CHUNK_REGISTRY.exists():
        with open(CHUNK_REGISTRY) as f:
            registry = json.load(f)
    else:
        registry = {'chunks': [], 'last_updated': None}
    
    # Add new chunks
    for chunk in chunks:
        # Remove existing chunk with same ID
        registry['chunks'] = [c for c in registry['chunks'] if c['id'] != chunk['id']]
        registry['chunks'].append(chunk)
    
    registry['last_updated'] = datetime.now().isoformat()
    
    CHUNK_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    with open(CHUNK_REGISTRY, 'w') as f:
        json.dump(registry, f, indent=2)
    
    return len(chunks)

def find_related_chunks(chunk_id, max_results=5):
    """Find semantically related chunks"""
    if not CHUNK_REGISTRY.exists():
        return []
    
    with open(CHUNK_REGISTRY) as f:
        registry = json.load(f)
    
    target = next((c for c in registry['chunks'] if c['id'] == chunk_id), None)
    if not target:
        return []
    
    # Simple scoring: shared domains + shared concepts
    scored = []
    for chunk in registry['chunks']:
        if chunk['id'] == chunk_id:
            continue
        
        score = 0
        # Domain overlap
        shared_domains = set(target['domains']) & set(chunk['domains'])
        score += len(shared_domains) * 2
        
        # Concept overlap
        shared_concepts = set(target['concepts']) & set(chunk['concepts'])
        score += len(shared_concepts) * 3
        
        # Type match
        if target['type'] == chunk['type']:
            score += 1
        
        if score > 0:
            scored.append((chunk, score))
    
    scored.sort(key=lambda x: x[1], reverse=True)
    return [c[0] for c in scored[:max_results]]

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Semantic Memory Chunker')
    parser.add_argument('--input', '-i', required=True, help='Input markdown file')
    parser.add_argument('--domains', '-d', help='Comma-separated domains')
    parser.add_argument('--output', '-o', help='Output JSON file (optional)')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: {input_path} not found")
        exit(1)
    
    content = input_path.read_text()
    domains = args.domains.split(',') if args.domains else []
    
    chunks = chunk_content(content, input_path, domains)
    count = register_chunks(chunks)
    
    print(f"Created {count} chunks from {input_path}")
    print(f"Registered in: {CHUNK_REGISTRY}")
    
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(chunks, f, indent=2)
        print(f"Saved to: {args.output}")
