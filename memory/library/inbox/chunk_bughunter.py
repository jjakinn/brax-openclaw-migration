# Read the transcript
with open('bug-hunter-methodology.txt', 'r') as f:
    content = f.read()

# Split into chunks of ~3000 words
words = content.split()
chunk_size = 3000
chunks = []

for i in range(0, len(words), chunk_size):
    chunk = ' '.join(words[i:i+chunk_size])
    chunks.append(chunk)

# Save chunks
for idx, chunk in enumerate(chunks):
    chunk_file = f'chunk_bughunter_{idx+1}.txt'
    with open(chunk_file, 'w') as f:
        f.write(chunk)
    print(f"Chunk {idx+1}: {len(chunk.split())} words -> {chunk_file}")

print(f"\nTotal: {len(chunks)} chunks from {len(words)} words")
