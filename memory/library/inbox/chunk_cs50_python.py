#!/usr/bin/env python3
import os

with open('cs50-python-course.txt', 'r') as f:
    words = f.read().split()

total = len(words)  # 183775 words
chunk_size = 15000  # ~12-13 chunks for 16 hours
os.makedirs('../knowledge-graph/corpus/by-source/cs50-python-2022/chunks', exist_ok=True)

num_chunks = (total + chunk_size - 1) // chunk_size
print(f"Creating {num_chunks} chunks...")

for i in range(num_chunks):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, total)
    chunk_words = words[start:end]
    chunk_text = ' '.join(chunk_words)
    
    with open(f'../knowledge-graph/corpus/by-source/cs50-python-2022/chunks/chunk_{i+1:03d}.txt', 'w') as f:
        f.write(chunk_text)
    print(f'Chunk {i+1}: {len(chunk_words)} words')

print(f'\n✅ {num_chunks} chunks created')
