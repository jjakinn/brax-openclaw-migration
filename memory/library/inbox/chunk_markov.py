#!/usr/bin/env python3
import os

with open("markov-chains.txt", "r") as f:
    words = f.read().split()

total = len(words)
chunk_size = 1370  # ~4 chunks
os.makedirs("../knowledge-graph/corpus/by-source/veritasium-markov-chains/chunks", exist_ok=True)

for i in range(4):
    start = i * chunk_size
    end = min((i + 1) * chunk_size, total)
    chunk = ' '.join(words[start:end])
    with open(f"../knowledge-graph/corpus/by-source/veritasium-markov-chains/chunks/chunk_{i+1:03d}.txt", "w") as f:
        f.write(chunk)
    print(f"Chunk {i+1}: {len(words[start:end])} words")

print(f"✅ 4 chunks created")
