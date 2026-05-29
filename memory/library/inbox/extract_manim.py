import re

with open('new-source10.en.vtt', 'r') as f:
    content = f.read()

# Parse VTT
lines = content.split('\n')
text_lines = []

for line in lines:
    line = line.strip()
    # Skip WEBVTT header, timing lines, cue numbers, and empty lines
    if not line or line == 'WEBVTT' or '-->' in line or re.match(r'^\d+$', line):
        continue
    # Skip style/region blocks
    if line.startswith('STYLE') or line.startswith('REGION'):
        continue
    text_lines.append(line)

# Join and clean
text = ' '.join(text_lines)
text = re.sub(r'\s+', ' ', text).strip()

with open('3b1b-manim-demo.txt', 'w') as f:
    f.write(text)

word_count = len(text.split())
print(f"Words: {word_count}")
print(f"First 300 chars: {text[:300]}")
