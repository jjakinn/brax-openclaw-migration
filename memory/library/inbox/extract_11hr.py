#!/usr/bin/env python3
import json

with open('video-11hr.en.json3', 'r') as f:
    data = json.load(f)

events = data.get('events', [])
print(f"Total events: {len(events)}")

# Get time range
if events:
    first_time = events[0].get('tStartMs', 0)
    last_time = events[-1].get('tStartMs', 0)
    print(f"First timestamp: {first_time/1000/60:.2f} min")
    print(f"Last timestamp: {last_time/1000/60:.2f} min")
    print(f"Duration: {(last_time - first_time)/1000/60:.2f} min")

# Extract all text
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
print(f"\nTotal words: {len(words)}")
print(f"Estimated minutes at 150 wpm: {len(words)/150:.1f}")

# Save
with open('video-11hr.txt', 'w') as f:
    f.write(full_text)
print("\n✅ Saved to video-11hr.txt")
