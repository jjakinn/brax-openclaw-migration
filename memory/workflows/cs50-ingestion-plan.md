# CS50 Full Course Ingestion - Revised Plan

## Problem Identified
The YouTube transcript extraction tool has limitations:
- Cannot resume from specific timestamps
- May timeout on very long videos (22+ hours)
- Extracted only first 2.5 hours automatically

## Better Approach for 22-Hour Content

### Option 1: Download Full Transcript First (RECOMMENDED)
```bash
# Download full transcript to file
yt-dlp --write-subs --write-auto-subs --skip-download \
  --sub-lang en --output cs50-full-course \
  "https://www.youtube.com/watch?v=gmuTjeQUbTM"

# This creates cs50-full-course.en.vtt (possibly 50+ MB)
# Drop this file in: memory/library/inbox/
```

Then I can:
- Process the file locally in 2-hour segments
- True checkpoint/resume capability
- No network timeouts
- Full 22 hours guaranteed

### Option 2: Use YouTube API with Paging
- Query transcript with time ranges
- More complex, still may have limits

### Option 3: Manual Segmentation
- Download video, split into parts
- Process each part separately
- Labor intensive

## Recommendation

**Use Option 1** - Download the .vtt transcript file:

1. Run the yt-dlp command above (or similar tool)
2. Place the .vtt file in `memory/library/inbox/`
3. I'll process it incrementally:
   - Read 2-hour chunks
   - Extract concepts
   - Checkpoint at 78%
   - Continue seamlessly

## Current Status
- ✅ 2.5 hours processed (Flask section)
- ⏳ 19.5 hours pending
- 📁 Ready to receive full transcript file

## Next Step
Download the full transcript and drop it in the inbox.
Then say "ingest" and I'll process the complete 22 hours.
