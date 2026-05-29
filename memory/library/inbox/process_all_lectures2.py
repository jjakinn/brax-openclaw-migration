#!/usr/bin/env python3
import json
import os
import re

# Process all stanford lecture files
files = [f for f in os.listdir('.') if re.match(r'stanford-cs106a-lec\d+\.en\.json3', f)]

for json_file in sorted(files):
    # Extract lecture number
    match = re.search(r'lec(\d+)\.en\.json3', json_file)
    if not match:
        continue
    
    lec_num = int(match.group(1))
    if lec_num < 7:  # Skip already processed
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

print("\n✅ All lectures processed")
