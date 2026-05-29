import os

chapters = [
    (2, "Gradient descent, how neural networks learn", 3171),
    (3, "Backpropagation, intuitively", 1936),
    (4, "Backpropagation calculus", 1632),
    (5, "Large Language Models explained briefly", 1113),
    (6, "Transformers, the tech behind LLMs", 4434),
    (7, "Attention in transformers, step-by-step", 4215),
    (8, "How might LLMs store facts", 4089),
    (9, "But how do AI images and videos actually work?", 6497)
]

total_chunks = 0
for ch_num, title, word_count in chapters:
    with open(f'3b1b-ch{ch_num}.txt', 'r') as f:
        content = f.read()
    
    words = content.split()
    chunk_size = 3000
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    
    for idx, chunk in enumerate(chunks):
        with open(f'chunk_3b1b_ch{ch_num}_{idx+1}.txt', 'w') as f:
            f.write(chunk)
    
    total_chunks += len(chunks)
    print(f"Chapter {ch_num}: {len(chunks)} chunks")

print(f"\nTotal: {total_chunks} chunks from 8 videos")
