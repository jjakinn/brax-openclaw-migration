#!/usr/bin/env python3
import json
import os

# Process lectures 7-28
for lec_num in range(7, 29):
    json_file = f'stanford-cs106a-lec{lec_num}.en.json3'
    
    if not os.path.exists(json_file):
        print(f"Skipping {json_file} - not found")
        continue
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    events = data.get('events', [])
    
    # Extract text
    all_text = []
    for event in events:
        if 'segs' in event:
            for seg in event['segs']:
                if 'utf8' in seg:
                    text = seg['utf8']
                    if text.strip():
                        all_text.append(text)
    
    full_text = ' '.join(all_text)
    words = full_text.split()
    word_count = len(words)
    
    # Save transcript
    txt_file = f'stanford-cs106a-lec{lec_num}.txt'
    with open(txt_file, 'w') as f:
        f.write(full_text)
    
    print(f"Lecture {lec_num}: {word_count} words")

print("\n✅ All lectures 7-28 processed")
