#!/usr/bin/env python3
import os

# Process all lecture txt files
for lec_num in range(7, 29):
    txt_file = f'stanford-cs106a-lec{lec_num}.txt'
    
    if not os.path.exists(txt_file):
        continue
    
    with open(txt_file, 'r') as f:
        words = f.read().split()
    
    total = len(words)
    chunk_size = 3500
    
    # Create directory
    chunk_dir = f'../knowledge-graph/corpus/by-source/stanford-cs106a-lec{lec_num}/chunks'
    os.makedirs(chunk_dir, exist_ok=True)
    
    # Create chunks
    num_chunks = (total + chunk_size - 1) // chunk_size
    for i in range(num_chunks):
        start = i * chunk_size
        end = min((i + 1) * chunk_size, total)
        chunk_words = words[start:end]
        chunk_text = ' '.join(chunk_words)
        
        with open(f'{chunk_dir}/chunk_{i+1:03d}.txt', 'w') as f:
            f.write(chunk_text)
    
    print(f"Lecture {lec_num}: {total} words, {num_chunks} chunks")

print("\n✅ All chunks created")
