# Project: ClawMind

## Description
My digital brain — an Obsidian vault for persistent memory as a knowledge graph.

## Key Patterns Learned

### Empty Note Problem
**Issue:** User clicked dots in graph view, many were empty.
**Solution:** Proactively fill ALL linked notes, not just obvious ones.
**Lesson:** Check for missing WikiLink targets, not just 0-byte files.

### File Naming Confusion
**Issue:** "Casino Build.md" vs "Casino Build Plan.md" — similar names, one empty.
**Solution:** Consolidate or clearly differentiate.
**Lesson:** Check for near-duplicate filenames.

### WikiLink Coverage
**Initial:** 34 notes, 85+ missing links
**After:** 73 notes, ~20 missing links
**Method:** Systematically created files for every missing link found.

## User Preferences
- **Quality:** Every note must have substance
- **Graph navigation:** No empty dots when clicking
- **Cross-linking:** Heavy use of [[WikiLinks]] for connections

## Related
- [[ClawMind]] — The vault itself
- [[Index]] — Dashboard
- [[Obsidian]] — The tool
