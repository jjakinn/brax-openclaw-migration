#!/usr/bin/env python3
import os

with open('markov-final.txt', 'r') as f:
    words = f.read().split()

total = len(words)  # 5429 words
chunk_size = 1357  # ~4 chunks
os.makedirs('../knowledge-graph/corpus/by-source/veritasium-markov-chains/chunks', exist_ok=True)

for i in range(4):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, total)
    chunk_words = words[start:end]
    chunk_text = ' '.join(chunk_words)
    
    with open(f'../knowledge-graph/corpus/by-source/veritasium-markov-chains/chunks/chunk_{i+1:03d}.txt', 'w') as f:
        f.write(chunk_text)
    print(f'Chunk {i+1}: {len(chunk_words)} words')

print(f'✅ Updated 4 chunks with full transcript')
