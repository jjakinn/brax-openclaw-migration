#!/usr/bin/env python3
"""
Knowledge Graph Ingestion Fixer
Moves pre-chunked content from library/inbox into the knowledge-graph structure.
Creates missing source directories and metadata files.
Updates chunk counts in metadata.
"""

import os
import json
import shutil
import glob
from pathlib import Path

WORKSPACE = "/Users/Jakin/.openclaw/workspace"
INBOX = f"{WORKSPACE}/memory/library/inbox"
KG_SOURCES = f"{WORKSPACE}/memory/knowledge-graph/corpus/by-source"

# Mapping: chunk prefix -> source directory name + display info
CHUNK_MAP = {
    "chunk_3b1b_ch2": ("3b1b-ch2-gradient-descent", "3Blue1Brown Ch2: Gradient Descent"),
    "chunk_3b1b_ch3": ("3b1b-ch3-backprop-intuitive", "3Blue1Brown Ch3: Backpropagation Intuitively"),
    "chunk_3b1b_ch4": ("3b1b-ch4-backprop-calculus", "3Blue1Brown Ch4: Backpropagation Calculus"),
    "chunk_3b1b_ch5": ("3b1b-ch5-llms-explained", "3Blue1Brown Ch5: LLMs Explained Briefly"),
    "chunk_3b1b_ch6": ("3b1b-ch6-transformers", "3Blue1Brown Ch6: Transformers"),
    "chunk_3b1b_ch7": ("3b1b-ch7-attention", "3Blue1Brown Ch7: Attention in Transformers"),
    "chunk_3b1b_ch8": ("3b1b-ch8-llm-facts", "3Blue1Brown Ch8: How LLMs Store Facts"),
    "chunk_3b1b_ch9": ("3b1b-ch9-ai-images-videos", "3Blue1Brown Ch9: AI Images & Videos"),
    "chunk_3b1b_1": ("3b1b-ch1-neural-network", "3Blue1Brown Ch1: What is a Neural Network?"),
    "chunk_agentic": ("agentic-workflows-course", "Agentic Workflows 6 Hour Course (Nick Saraev)"),
    "chunk_aihardway": ("ai-hard-way-networkchuck", "You've Been Using AI the Hard Way (NetworkChuck)"),
    "chunk_android": ("android-hacking-workshop", "Android Hacking Workshop (B3nacSec)"),
    "chunk_appanalysis": ("bug-hunter-app-analysis", "Bug Hunter's Methodology - Application Analysis"),
    "chunk_bughunter": ("bug-hunter-methodology", "The Bug Hunter's Methodology (Jason Haddix)"),
    "chunk_claude_code": ("claude-code-course", "Claude Code Full Course 4 Hours (Nick Saraev)"),
    "chunk_claude_phone": ("claude-phone-calls", "Free Phone Calls with Claude Code (NetworkChuck)"),
    "chunk_darkweb": ("darkweb-exposed", "The Dark Web Exposed (NetworkChuck)"),
    "chunk_jshackers": ("hacker101-javascript", "Hacker101 - JavaScript for Hackers (STOKfredrik)"),
    "chunk_manim": ("manim-3b1b-demo", "How I Animate 3Blue1Brown (Manim Demo)"),
    "chunk_manualhack": ("manual-hacking-guide", "Manual Hacking Full Guide (JakSec)"),
    "chunk_mcp": ("mcp-networkchuck", "You Need to Learn MCP RIGHT NOW (NetworkChuck)"),
    "chunk_n8n": ("n8n-tutorial-zero-to-hero", "n8n Tutorial Zero to Hero (freeCodeCamp)"),
    "chunk_networkchuck": ("networkchuck-mitm-attack", "NetworkChuck MiTM Attack"),
    "chunk_nnscratch": ("neural-network-scratch", "I Built a Neural Network from Scratch (Green Code)"),
    "chunk_openclaw_6hr": ("openclaw-6hour-course", "OpenClaw AI Full 6 Hour Course (Julian Goldie)"),
    "chunk_openclaw_army": ("openclaw-army-agents", "How to Build an Army of OpenClaw Agents (Alex Finn)"),
    "chunk_openclaw_condensed": ("openclaw-condensed-lessons", "100 Hours of OpenClaw Lessons in 35 Min (Alex Finn)"),
    "chunk_openclaw_fixed": ("openclaw-fixed-setup", "I Fixed OpenClaw So It Actually Works (Greg Isenberg)"),
    "chunk_openclaw_master": ("openclaw-master-10hr", "Master OpenClaw in 10 Hours (Mani Kanasani)"),
    "chunk_openclaw_money": ("openclaw-making-money", "Making $$$ with OpenClaw (Greg Isenberg)"),
    "chunk_osint5min": ("osint-5min-overview", "Every OSINT Technique in 5 Minutes"),
    "chunk_osint_full": ("osint-full-course", "OSINT Full Course 5 Hours (The Cyber Mentor)"),
    "chunk_osint_1": ("osint-beginners", "OSINT for Beginners (Loi Liang Yang)"),
    "chunk_prompting": ("prompting-ai-networkchuck", "You Suck at Prompting AI (NetworkChuck)"),
    "chunk_recon": ("live-recon-snapchat", "Live Recon on Snapchat (ITSecurityGuard)"),
}

# Raw transcripts that need to be chunked (no pre-chunked files exist)
RAW_TRANSCRIPT_MAP = {
    "cpp-course.txt": ("cpp-course-beginner-advanced", "C++ Programming Course (31 hrs)"),
    "generative-ai-course.txt": ("generative-ai-full-course", "Generative AI Full Course (30 hrs)"),
    "cs50-python-course.txt": ("cs50-python-2022", "CS50 Python Course (16 hrs)"),
    "java-course.txt": ("java-full-course", "Java Full Course (2.5 hrs)"),
    "video-11hr.txt": ("numerology-divine-triangle-1979", "Numerology and the Divine Triangle (11 hrs)"),
    "new-video.txt": ("numerology-beginners", "Numerology For Beginners (3.3 hrs)"),
}

# Stanford lectures 1-6 that are missing chunks
STANFORD_MISSING = [1, 2, 3, 4, 5, 6]

stats = {
    "sources_created": 0,
    "chunks_moved": 0,
    "chunks_created": 0,
    "metadata_updated": 0,
    "errors": [],
}

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def chunk_text(text, chunk_size=5000):
    """Split text into chunks of approximately chunk_size words."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_words = words[i:i + chunk_size]
        chunks.append(" ".join(chunk_words))
    return chunks

def create_metadata(source_dir, source_id, display_name, chunk_count, total_words=0):
    """Create or update metadata.json for a source."""
    meta_path = os.path.join(source_dir, "metadata.json")
    
    if os.path.exists(meta_path):
        with open(meta_path, 'r') as f:
            meta = json.load(f)
        # Update chunk counts
        if "metadata" in meta:
            meta["metadata"]["chunks_processed"] = chunk_count
            meta["metadata"]["ingestion_status"] = "COMPLETE"
        if "length" in meta:
            meta["length"]["chunk_count"] = chunk_count
    else:
        meta = {
            "source_id": source_id,
            "display_name": display_name,
            "type": "video",
            "format": "video",
            "metadata": {
                "ingested_date": "2026-03-23",
                "ingestion_status": "COMPLETE",
                "total_words": total_words,
                "total_chunks": chunk_count,
                "chunks_processed": chunk_count,
            },
            "domains": [],
            "files": {
                "chunks": "chunks/"
            }
        }
    
    with open(meta_path, 'w') as f:
        json.dump(meta, f, indent=2)
    return meta

def move_prechunked_files():
    """Move pre-chunked files from inbox to knowledge graph structure."""
    print("=" * 60)
    print("PHASE 1: Moving pre-chunked files from inbox")
    print("=" * 60)
    
    inbox_files = glob.glob(f"{INBOX}/chunk_*.txt")
    
    # Group files by their prefix
    grouped = {}
    for fpath in inbox_files:
        fname = os.path.basename(fpath)
        # Find which prefix this belongs to
        matched = False
        for prefix, (dir_name, display_name) in sorted(CHUNK_MAP.items(), key=lambda x: -len(x[0])):
            # Match prefix exactly: chunk_name_N.txt
            base = fname.replace(".txt", "")
            if base.startswith(prefix + "_") or base == prefix:
                if dir_name not in grouped:
                    grouped[dir_name] = {"display": display_name, "files": []}
                grouped[dir_name]["files"].append(fpath)
                matched = True
                break
        if not matched:
            stats["errors"].append(f"No mapping for: {fname}")
    
    for dir_name, info in sorted(grouped.items()):
        source_dir = os.path.join(KG_SOURCES, dir_name)
        chunks_dir = os.path.join(source_dir, "chunks")
        ensure_dir(chunks_dir)
        
        files = sorted(info["files"])
        total_words = 0
        
        for i, fpath in enumerate(files, 1):
            dest = os.path.join(chunks_dir, f"chunk_{i:03d}.txt")
            shutil.copy2(fpath, dest)
            with open(dest, 'r') as f:
                content = f.read()
                total_words += len(content.split())
            stats["chunks_moved"] += 1
        
        create_metadata(source_dir, dir_name, info["display"], len(files), total_words)
        stats["sources_created"] += 1
        stats["metadata_updated"] += 1
        print(f"  ✅ {dir_name}: {len(files)} chunks ({total_words:,} words)")

def chunk_raw_transcripts():
    """Chunk raw transcript files that don't have pre-chunked versions."""
    print("\n" + "=" * 60)
    print("PHASE 2: Chunking raw transcripts")
    print("=" * 60)
    
    for filename, (dir_name, display_name) in RAW_TRANSCRIPT_MAP.items():
        raw_path = os.path.join(INBOX, filename)
        if not os.path.exists(raw_path):
            stats["errors"].append(f"Raw transcript not found: {filename}")
            continue
        
        source_dir = os.path.join(KG_SOURCES, dir_name)
        chunks_dir = os.path.join(source_dir, "chunks")
        
        # Check if chunks already exist
        existing_chunks = glob.glob(os.path.join(chunks_dir, "chunk_*.txt")) if os.path.exists(chunks_dir) else []
        if existing_chunks:
            print(f"  ⏭️  {dir_name}: already has {len(existing_chunks)} chunks, skipping")
            continue
        
        ensure_dir(chunks_dir)
        
        with open(raw_path, 'r', errors='replace') as f:
            text = f.read()
        
        total_words = len(text.split())
        chunks = chunk_text(text, 5000)
        
        for i, chunk in enumerate(chunks, 1):
            dest = os.path.join(chunks_dir, f"chunk_{i:03d}.txt")
            with open(dest, 'w') as f:
                f.write(chunk)
            stats["chunks_created"] += 1
        
        create_metadata(source_dir, dir_name, display_name, len(chunks), total_words)
        stats["sources_created"] += 1
        stats["metadata_updated"] += 1
        print(f"  ✅ {dir_name}: {len(chunks)} chunks from {total_words:,} words")

def fix_stanford_missing():
    """Chunk Stanford CS106A lectures 1-6 from raw transcripts."""
    print("\n" + "=" * 60)
    print("PHASE 3: Fixing Stanford CS106A lectures 1-6")
    print("=" * 60)
    
    for lec_num in STANFORD_MISSING:
        raw_path = os.path.join(INBOX, f"stanford-cs106a-lec{lec_num}.txt")
        if not os.path.exists(raw_path):
            stats["errors"].append(f"Stanford lec{lec_num} transcript not found")
            continue
        
        dir_name = f"stanford-cs106a-lec{lec_num}"
        source_dir = os.path.join(KG_SOURCES, dir_name)
        chunks_dir = os.path.join(source_dir, "chunks")
        
        existing_chunks = glob.glob(os.path.join(chunks_dir, "chunk_*.txt")) if os.path.exists(chunks_dir) else []
        if existing_chunks:
            print(f"  ⏭️  {dir_name}: already has {len(existing_chunks)} chunks")
            continue
        
        ensure_dir(chunks_dir)
        
        with open(raw_path, 'r', errors='replace') as f:
            text = f.read()
        
        total_words = len(text.split())
        chunks = chunk_text(text, 5000)
        
        for i, chunk in enumerate(chunks, 1):
            dest = os.path.join(chunks_dir, f"chunk_{i:03d}.txt")
            with open(dest, 'w') as f:
                f.write(chunk)
            stats["chunks_created"] += 1
        
        create_metadata(source_dir, dir_name, f"Stanford CS106A Lecture {lec_num}", len(chunks), total_words)
        stats["metadata_updated"] += 1
        print(f"  ✅ {dir_name}: {len(chunks)} chunks from {total_words:,} words")

def update_existing_metadata():
    """Update metadata for sources that already have chunks but show 0 processed."""
    print("\n" + "=" * 60)
    print("PHASE 4: Updating existing source metadata")
    print("=" * 60)
    
    for source_dir_path in sorted(glob.glob(f"{KG_SOURCES}/*/")):
        dir_name = os.path.basename(source_dir_path.rstrip('/'))
        chunks_dir = os.path.join(source_dir_path, "chunks")
        meta_path = os.path.join(source_dir_path, "metadata.json")
        
        if not os.path.exists(meta_path):
            continue
        
        chunk_files = glob.glob(os.path.join(chunks_dir, "*.txt")) if os.path.exists(chunks_dir) else []
        # Also check for full-transcript.txt
        full_transcript = os.path.join(chunks_dir, "full-transcript.txt")
        
        if not chunk_files and not os.path.exists(full_transcript):
            continue
        
        total_words = 0
        for cf in chunk_files:
            with open(cf, 'r', errors='replace') as f:
                total_words += len(f.read().split())
        
        if os.path.exists(full_transcript) and not chunk_files:
            with open(full_transcript, 'r', errors='replace') as f:
                total_words = len(f.read().split())
            chunk_count = 1
        else:
            chunk_count = len(chunk_files)
        
        with open(meta_path, 'r') as f:
            meta = json.load(f)
        
        updated = False
        if "metadata" in meta:
            if meta["metadata"].get("chunks_processed", 0) != chunk_count:
                meta["metadata"]["chunks_processed"] = chunk_count
                meta["metadata"]["ingestion_status"] = "COMPLETE"
                if total_words > 0:
                    meta["metadata"]["total_words"] = total_words
                updated = True
        
        if updated:
            with open(meta_path, 'w') as f:
                json.dump(meta, f, indent=2)
            stats["metadata_updated"] += 1
            print(f"  🔧 {dir_name}: updated to {chunk_count} chunks, {total_words:,} words")

def handle_special_sources():
    """Handle sources with special inbox file names."""
    print("\n" + "=" * 60)
    print("PHASE 5: Special source handling")
    print("=" * 60)
    
    # Attacking AI v1.1 - check for raw transcript
    special = {
        "hacker101-javascript.txt": ("hacker101-javascript-hackers", "Hacker101 - JavaScript for Hackers (STOKfredrik)"),
        "osint-beginners.txt": ("osint-beginners", "OSINT for Beginners (Loi Liang Yang)"),
        "osint-5min.txt": ("osint-5min-overview", "Every OSINT Technique in 5 Minutes"),
        "android-hacking-workshop.txt": ("android-hacking-workshop", "Android Hacking Workshop (B3nacSec)"),
        "neural-network-scratch.txt": ("neural-network-scratch", "I Built a Neural Network from Scratch"),
        "3b1b-ch3.txt": ("3b1b-ch3-backprop-intuitive", "3Blue1Brown Ch3: Backpropagation Intuitively"),
        "3b1b-ch4.txt": ("3b1b-ch4-backprop-calculus", "3Blue1Brown Ch4: Backpropagation Calculus"),
        "3b1b-ch5.txt": ("3b1b-ch5-llms-explained", "3Blue1Brown Ch5: LLMs Explained Briefly"),
        "3b1b-ch9.txt": ("3b1b-ch9-ai-images-videos", "3Blue1Brown Ch9: AI Images & Videos"),
        "bug-hunter-methodology.txt": ("bug-hunter-methodology", "The Bug Hunter's Methodology (Jason Haddix)"),
        "live-recon-snapchat.txt": ("live-recon-snapchat", "Live Recon on Snapchat (ITSecurityGuard)"),
        "manual-hacking-guide.txt": ("manual-hacking-guide", "Manual Hacking Full Guide (JakSec)"),
        "network-chuck-hacking-guide.txt": ("networkchuck-mitm-attack", "NetworkChuck MiTM Attack"),
    }
    
    for filename, (dir_name, display_name) in special.items():
        raw_path = os.path.join(INBOX, filename)
        if not os.path.exists(raw_path):
            continue
        
        source_dir = os.path.join(KG_SOURCES, dir_name)
        chunks_dir = os.path.join(source_dir, "chunks")
        
        # Only process if no chunks exist yet
        existing = glob.glob(os.path.join(chunks_dir, "*.txt")) if os.path.exists(chunks_dir) else []
        if existing:
            continue
        
        ensure_dir(chunks_dir)
        # Copy as full transcript
        dest = os.path.join(chunks_dir, "full-transcript.txt")
        shutil.copy2(raw_path, dest)
        
        with open(raw_path, 'r', errors='replace') as f:
            total_words = len(f.read().split())
        
        create_metadata(source_dir, dir_name, display_name, 1, total_words)
        stats["sources_created"] += 1
        print(f"  ✅ {dir_name}: full transcript ({total_words:,} words)")

def verify():
    """Verify all sources and report final state."""
    print("\n" + "=" * 60)
    print("VERIFICATION")
    print("=" * 60)
    
    total_sources = 0
    total_chunks = 0
    total_words = 0
    complete = 0
    empty = 0
    
    for source_dir_path in sorted(glob.glob(f"{KG_SOURCES}/*/")):
        dir_name = os.path.basename(source_dir_path.rstrip('/'))
        chunks_dir = os.path.join(source_dir_path, "chunks")
        meta_path = os.path.join(source_dir_path, "metadata.json")
        
        total_sources += 1
        
        chunk_files = []
        if os.path.exists(chunks_dir):
            chunk_files = [f for f in os.listdir(chunks_dir) if f.endswith('.txt')]
        
        source_words = 0
        for cf in chunk_files:
            with open(os.path.join(chunks_dir, cf), 'r', errors='replace') as f:
                source_words += len(f.read().split())
        
        if chunk_files:
            complete += 1
            total_chunks += len(chunk_files)
            total_words += source_words
            status = "✅"
        else:
            empty += 1
            status = "❌"
        
        # Verify metadata matches
        meta_ok = "?"
        if os.path.exists(meta_path):
            with open(meta_path, 'r') as f:
                meta = json.load(f)
            meta_chunks = meta.get("metadata", {}).get("chunks_processed", 0)
            meta_status = meta.get("metadata", {}).get("ingestion_status", "UNKNOWN")
            if meta_chunks == len(chunk_files) and (meta_status == "COMPLETE" or len(chunk_files) == 0):
                meta_ok = "✅"
            else:
                meta_ok = f"⚠️ (meta says {meta_chunks}, actual {len(chunk_files)}, status={meta_status})"
        else:
            meta_ok = "❌ no metadata"
        
        print(f"  {status} {dir_name}: {len(chunk_files)} chunks, {source_words:,} words | meta: {meta_ok}")
    
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")
    print(f"  Total sources:     {total_sources}")
    print(f"  With content:      {complete} ✅")
    print(f"  Still empty:       {empty} ❌")
    print(f"  Total chunks:      {total_chunks}")
    print(f"  Total words:       {total_words:,}")
    print(f"  Sources created:   {stats['sources_created']}")
    print(f"  Chunks moved:      {stats['chunks_moved']}")
    print(f"  Chunks created:    {stats['chunks_created']}")
    print(f"  Metadata updated:  {stats['metadata_updated']}")
    if stats["errors"]:
        print(f"\n  ERRORS ({len(stats['errors'])}):")
        for e in stats["errors"]:
            print(f"    ⚠️  {e}")

if __name__ == "__main__":
    print("Knowledge Graph Ingestion Fixer")
    print("=" * 60)
    move_prechunked_files()
    chunk_raw_transcripts()
    fix_stanford_missing()
    handle_special_sources()
    update_existing_metadata()
    verify()
