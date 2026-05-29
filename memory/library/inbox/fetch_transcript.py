#!/usr/bin/env python3
import urllib.request
import urllib.parse
import json
import re

video_id = "KZeIEiBrT_w"

url = f"https://www.youtube.com/watch?v={video_id}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

match = re.search(r'ytInitialPlayerResponse\s*=\s*({.+?});', html)
if match:
    data = json.loads(match.group(1))
    captions = data.get('captions', {}).get('captionTracks', [])
    print(f"Found {len(captions)} caption tracks:")
    for cap in captions:
        print(f"  - {cap.get('languageCode')}: {cap.get('name', {}).get('simpleText', 'unknown')}")
        if cap.get('baseUrl'):
            try:
                cap_req = urllib.request.Request(cap['baseUrl'], headers=headers)
                with urllib.request.urlopen(cap_req) as cap_response:
                    cap_xml = cap_response.read().decode('utf-8')
                    text_entries = re.findall(r'>([^<]+)</text', cap_xml)
                    words = ' '.join(text_entries).split()
                    print(f"    Words: {len(words)}")
            except Exception as e:
                print(f"    Error: {e}")
else:
    print("Could not find player response")
