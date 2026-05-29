with open('openclaw-making-money.txt', 'r') as f:
    content = f.read()

words = content.split()
chunk_size = 3000
chunks = []

for i in range(0, len(words), chunk_size):
    chunk = ' '.join(words[i:i+chunk_size])
    chunks.append(chunk)

for idx, chunk in enumerate(chunks):
    with open(f'chunk_openclaw_money_{idx+1}.txt', 'w') as f:
        f.write(chunk)
    print(f"Chunk {idx+1}: {len(chunk.split())} words")

print(f"Total: {len(chunks)} chunks from {len(words)} words")
