#!/usr/bin/env python3
"""Fast YouTube transcript fetcher using youtube_transcript_api (v0.6+)."""
import sys
import re

from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_id_or_url, languages=["en"]):
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

    try:
        # v0.6+ API
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id, languages=languages)
    except Exception as e:
        print(f"Error fetching transcript: {e}", file=sys.stderr)
        sys.exit(1)

    # Concatenate all text entries
    full_text = " ".join(entry.text for entry in transcript)
    print(full_text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 fast_yt_transcript.py <URL or video_id> [lang1,lang2,...]", file=sys.stderr)
        sys.exit(1)
    video = sys.argv[1]
    langs = sys.argv[2].split(",") if len(sys.argv) > 2 else ["en"]
    fetch_transcript(video, langs)
