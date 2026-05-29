import json
import re

# Read the JSON3 file
with open('new-source.en.json3', 'r') as f:
    data = json.load(f)

# Extract events
all_text = []
for event in data.get('events', []):
    if 'segs' in event:
        for seg in event['segs']:
            if 'utf8' in seg:
                text = seg['utf8']
                # Skip music notes and other non-speech markers
                if text.strip() and not re.match(r'^[♪\s]+$', text):
                    all_text.append(text)

# Join and clean
transcript = ''.join(all_text)
transcript = re.sub(r'\s+', ' ', transcript).strip()

# Save
clean_filename = 'bug-hunter-methodology.txt'
with open(clean_filename, 'w') as f:
    f.write(transcript)

word_count = len(transcript.split())
print(f"Cleaned transcript saved to: {clean_filename}")
print(f"Total words: {word_count}")
