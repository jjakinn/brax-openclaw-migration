#!/usr/bin/env python3
"""
Memory Priority Manager
Auto-promote/demote memories based on access patterns
"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path

MEMORY_DIR = Path("/Users/Jakin/.openclaw/workspace/memory")
ACCESS_LOG = MEMORY_DIR / "knowledge-graph/index/access-log.json"
PRIORITY_SCHEMA = MEMORY_DIR / "knowledge-graph/ontology/priority-schema.json"

def load_json(path):
    if not path.exists():
        return {}
    with open(path) as f:
        return json.load(f)

def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def track_access(memory_id, query_context="", user_rating=None):
    """Log a memory access event"""
    log = load_json(ACCESS_LOG)
    if "accesses" not in log:
        log["accesses"] = []
    
    log["accesses"].append({
        "memory_id": memory_id,
        "accessed_at": datetime.now().isoformat(),
        "query_context": query_context,
        "user_rating": user_rating
    })
    
    # Keep only last 1000 accesses
    log["accesses"] = log["accesses"][-1000:]
    save_json(ACCESS_LOG, log)

def get_access_count(memory_id, days=30):
    """Count accesses for a memory in last N days"""
    log = load_json(ACCESS_LOG)
    cutoff = datetime.now() - timedelta(days=days)
    
    count = 0
    for entry in log.get("accesses", []):
        if entry["memory_id"] == memory_id:
            access_time = datetime.fromisoformat(entry["accessed_at"])
            if access_time > cutoff:
                count += 1
    return count

def get_last_access(memory_id):
    """Get last access time for a memory"""
    log = load_json(ACCESS_LOG)
    last = None
    
    for entry in log.get("accesses", []):
        if entry["memory_id"] == memory_id:
            access_time = datetime.fromisoformat(entry["accessed_at"])
            if last is None or access_time > last:
                last = access_time
    return last

def suggest_priority_update(memory_id, current_priority):
    """Suggest priority change based on access patterns"""
    schema = load_json(PRIORITY_SCHEMA)
    
    access_30d = get_access_count(memory_id, days=30)
    last_access = get_last_access(memory_id)
    
    if current_priority == "P2" and access_30d >= 5:
        return "P1", f"High access ({access_30d}x in 30d) — promote to P1"
    
    if current_priority == "P1" and last_access:
        days_since = (datetime.now() - last_access).days
        if days_since > 90:
            return "P2", f"Stale ({days_since}d since access) — demote to P2"
    
    return None, None

def scan_memories_for_updates():
    """Scan all memory files for priority updates"""
    updates = []
    
    # Scan MEMORY.md
    memory_file = MEMORY_DIR / "MEMORY.md"
    if memory_file.exists():
        content = memory_file.read_text()
        # Look for priority markers and suggest updates
        # This is a simplified version — full implementation would parse structure
        
    return updates

if __name__ == "__main__":
    print("Memory Priority Manager")
    print("=" * 50)
    
    # Example: Track an access
    # track_access("powerapps-cli-config", "How to deploy Code Apps")
    
    # Example: Check promotion candidate
    # new_priority, reason = suggest_priority_update("some-id", "P2")
    
    print("Priority schema loaded from:", PRIORITY_SCHEMA)
    print("Access log:", ACCESS_LOG)
    print("\nTo track access programmatically:")
    print("  from priority_manager import track_access")
    print("  track_access('memory-id', 'query context')")
