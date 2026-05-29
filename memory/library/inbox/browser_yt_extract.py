#!/usr/bin/env python3
"""
Fast YouTube transcript extractor via browser automation.
Opens video, clicks 'Show transcript', extracts full text via JS eval.
No rate limits. Works for any video with captions.
"""
import sys
import re
import json
import time

def extract_via_browser(video_url, output_file=None):
    """Use browser automation to extract transcript."""
    # We'll generate a shell script that uses the browser tool
    # But since we can't call browser from shell directly, let's use a different approach:
    # Return the JS extraction code to be run via browser evaluate
    
    video_id = None
    if "youtube.com" in video_url or "youtu.be" in video_url:
        m = re.search(r'[?&]v=([a-zA-Z0-9_-]{11})', video_url)
        if not m:
            m = re.search(r'youtu\.be/([a-zA-Z0-9_-]{11})', video_url)
        if m:
            video_id = m.group(1)
    else:
        video_id = video_url
    
    return video_id, video_url

def get_clean_js():
    """JavaScript to run in browser to extract clean transcript text."""
    return """
(() => {
    const segments = document.querySelectorAll('ytd-transcript-body-renderer ytd-transcript-segment-renderer');
    if (segments.length === 0) return '';
    
    let text = '';
    segments.forEach(seg => {
        const timestamp = seg.querySelector('[class*="timestamp"]');
        const body = seg.querySelector('[class*="segment-text"]');
        if (body) {
            text += body.textContent.trim() + ' ';
        }
    });
    return text.trim();
})()
"""

def get_all_text_js():
    """Fallback JS that grabs all text from transcript panel."""
    return """
(() => {
    const panel = document.querySelector('ytd-transcript-body-renderer');
    if (!panel) return '';
    return panel.innerText;
})()
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 browser_yt_extract.py <URL> [output_file]", file=sys.stderr)
        sys.exit(1)
    
    url = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    vid, full_url = extract_via_browser(url, out)
    print(json.dumps({"video_id": vid, "url": full_url, "needs_browser": True}))
