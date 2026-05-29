#!/usr/bin/env python3
import os
import json

# Read the full transcript
with open("cs50-full-course.txt", "r") as f:
    text = f.read()

words = text.split()
total_words = len(words)
print(f"Total words: {total_words}")

# Process in 15,000 word chunks (roughly 2-hour segments)
chunk_size = 15000
num_chunks = (total_words + chunk_size - 1) // chunk_size
print(f"Creating {num_chunks} chunks")

# Create chunk info
chunk_info = []
for i in range(num_chunks):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, total_words)
    chunk_words = words[start:end]
    chunk_text = ' '.join(chunk_words)
    
    chunk_file = f"chunk_{i+1:03d}.txt"
    chunk_path = f"../knowledge-graph/corpus/by-source/cs50-full-course/chunks/{chunk_file}"
    
    # Write chunk
    os.makedirs(os.path.dirname(chunk_path), exist_ok=True)
    with open(chunk_path, "w") as f:
        f.write(chunk_text)
    
    chunk_info.append({
        "chunk_id": i + 1,
        "file": chunk_file,
        "word_count": len(chunk_words),
        "start_word": start,
        "end_word": end
    })
    print(f"  Chunk {i+1}: {len(chunk_words)} words")

# Save chunk manifest
manifest = {
    "source_id": "cs50-full-course-2026",
    "total_words": total_words,
    "total_chunks": num_chunks,
    "chunk_size": chunk_size,
    "chunks": chunk_info
}

with open("../knowledge-graph/corpus/by-source/cs50-full-course/chunk-manifest.json", "w") as f:
    json.dump(manifest, f, indent=2)

print(f"\n✅ Created {num_chunks} chunks")
