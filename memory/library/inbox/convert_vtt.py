#!/usr/bin/env python3
import re

with open("cs50-full-course.en.vtt", "r") as f:
    content = f.read()

# Clean VTT to plain text
lines = content.splitlines()
text_lines = []
seen = set()

timestamp_pattern = re.compile(r'\d{2}:\d{2}:\d{2}\.\d{3}')

for line in lines:
    line = line.strip()
    if not line or line == 'WEBVTT' or line.isdigit():
        continue
    if timestamp_pattern.match(line) or '-->' in line:
        continue
    if line.startswith('NOTE') or line.startswith('STYLE'):
        continue
    line = re.sub(r'<[^>]+>', '', line)
    if line in seen:
        continue
    seen.add(line)
    text_lines.append(line)

output = '\n'.join(text_lines)
with open("cs50-full-course.txt", "w") as f:
    f.write(output)

print(f"Converted: {len(output)} characters, {len(text_lines)} lines")
