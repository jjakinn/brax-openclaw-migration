#!/usr/bin/env python3
"""Lightweight YouTube transcript fetcher — scrapes ytInitialPlayerResponse directly."""
import sys
import urllib.request
import json
import re

def fetch_transcript(video_id_or_url, language="en"):
    # Extract video ID
    if "youtube.com" in video_id_or_url or "youtu.be" in video_id_or_url:
        m = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', video_id_or_url)
        if not m:
            m = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', video_id_or_url)
        if not m:
            print("Could not extract video ID from URL", file=sys.stderr)
            sys.exit(1)
        video_id = m.group(1)
    else:
        video_id = video_id_or_url

    url = f"https://www.youtube.com/watch?v={video_id}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "identity",
        "DNT": "1",
        "Connection": "keep-alive",
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching page: {e}", file=sys.stderr)
        sys.exit(1)

    # Extract ytInitialPlayerResponse
    match = re.search(r'ytInitialPlayerResponse\s*=\s*({.+?});\s*</script>', html, re.DOTALL)
    if not match:
        print("Could not find ytInitialPlayerResponse in page", file=sys.stderr)
        sys.exit(1)

    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}", file=sys.stderr)
        sys.exit(1)

    captions = data.get('captions', {}).get('captionTracks', [])
    if not captions:
        print("No captions available for this video", file=sys.stderr)
        sys.exit(1)

    # Find best caption track
    best = None
    for cap in captions:
        if cap.get('languageCode') == language:
            best = cap
            break
    if not best:
        # Try any English variant
        for cap in captions:
            if cap.get('languageCode', '').startswith('en'):
                best = cap
                break
    if not best:
        best = captions[0]  # Fallback to first available

    cap_url = best.get('baseUrl')
    if not cap_url:
        print("No caption URL found", file=sys.stderr)
        sys.exit(1)

    # Fetch caption XML
    cap_req = urllib.request.Request(cap_url, headers=headers)
    try:
        with urllib.request.urlopen(cap_req, timeout=30) as cap_response:
            cap_xml = cap_response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching captions: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse XML — YouTube uses 
    # <text start="0.00" dur="3.00">Hello world</text>
    entries = re.findall(r'<text[^>]*>([^<]+)</text>', cap_xml)
    transcript = ' '.join(entries)
    print(transcript)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_yt_transcript.py <URL or video_id> [language]", file=sys.stderr)
        sys.exit(1)
    video = sys.argv[1]
    lang = sys.argv[2] if len(sys.argv) > 2 else "en"
    fetch_transcript(video, lang)
