import json
import re

with open('new-source11.en.json3', 'r') as f:
    data = json.load(f)

all_text = []
for event in data.get('events', []):
    if 'segs' in event:
        for seg in event['segs']:
            if 'utf8' in seg:
                text = seg['utf8']
                if text.strip() and not re.match(r'^[♪\s]+$', text):
                    all_text.append(text)

transcript = ''.join(all_text)
transcript = re.sub(r'\s+', ' ', transcript).strip()

with open('manual-hacking-guide.txt', 'w') as f:
    f.write(transcript)

word_count = len(transcript.split())
print(f"Words: {word_count}")
