import json
import re
import os

# Video info mapping
videos = {
    2: {"title": "Gradient descent, how neural networks learn", "duration": 21},
    3: {"title": "Backpropagation, intuitively", "duration": 13},
    4: {"title": "Backpropagation calculus", "duration": 11},
    5: {"title": "Large Language Models explained briefly", "duration": 6},
    6: {"title": "Transformers, the tech behind LLMs", "duration": 26},
    7: {"title": "Attention in transformers, step-by-step", "duration": 24},
    8: {"title": "How might LLMs store facts", "duration": 15},
    9: {"title": "But how do AI images and videos actually work?", "duration": 22}
}

def extract_from_json3(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    all_text = []
    for event in data.get('events', []):
        if 'segs' in event:
            for seg in event['segs']:
                if 'utf8' in seg:
                    text = seg['utf8']
                    if text.strip() and not re.match(r'^[♪\s]+$', text):
                        all_text.append(text)
    return ''.join(all_text)

def extract_from_vtt(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    # Remove WEBVTT header and timing lines
    lines = content.split('\n')
    text_lines = []
    for line in lines:
        line = line.strip()
        # Skip empty lines, WEBVTT header, and timing lines (contain -->)
        if not line or line == 'WEBVTT' or '-->' in line:
            continue
        # Skip cue numbers (just numbers)
        if re.match(r'^\d+$', line):
            continue
        text_lines.append(line)
    return ' '.join(text_lines)

total_words = 0
results = []

for ch_num in range(2, 10):
    json3_file = f'3b1b-ch{ch_num}.en.json3'
    vtt_file = f'3b1b-ch{ch_num}.en.vtt'
    
    if os.path.exists(json3_file):
        text = extract_from_json3(json3_file)
    elif os.path.exists(vtt_file):
        text = extract_from_vtt(vtt_file)
    else:
        print(f"Warning: No file found for chapter {ch_num}")
        continue
    
    # Clean up
    text = re.sub(r'\s+', ' ', text).strip()
    word_count = len(text.split())
    total_words += word_count
    
    # Save to file
    output_file = f'3b1b-ch{ch_num}.txt'
    with open(output_file, 'w') as f:
        f.write(text)
    
    results.append({
        'chapter': ch_num,
        'title': videos[ch_num]['title'],
        'words': word_count,
        'file': output_file
    })
    print(f"Chapter {ch_num}: {videos[ch_num]['title'][:50]}... - {word_count} words")

print(f"\nTotal words: {total_words}")
print(f"\nAll transcripts saved!")
