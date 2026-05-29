# ClawMind Auto-Learning Engine — Complete Setup

## Overview

An n8n-powered automation system that continuously updates, adds to, and learns from your Obsidian knowledge graph.

**Status:** ✅ Configured (Ready to activate)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT SOURCES                           │
├─────────────────────────────────────────────────────────────┤
│  • Conversation Webhook    → clawmind-conversation-capture  │
│  • File Inbox (~/ClawMind/inbox/*.md)                     │
│  • Manual Trigger          → Immediate processing           │
│  • Scheduled (15min)       → Auto-processing                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   PROCESSING PIPELINE                      │
├─────────────────────────────────────────────────────────────┤
│  1. Extract Metadata                                        │
│     - Parse frontmatter                                     │
│     - Extract WikiLinks                                     │
│     - Identify topics                                       │
│     - Classify note type                                    │
│                                                             │
│  2. Deduplication                                           │
│     - Check for existing notes                              │
│     - Skip if duplicate                                     │
│     - Merge if related                                      │
│                                                             │
│  3. Route Action                                            │
│     - Create new note   → Write to ~/ClawMind/*.md         │
│     - Update existing   → Append new content                │
│                                                             │
│  4. Update Index                                            │
│     - Increment graph stats                                 │
│     - Add to appropriate section                            │
│     - Update backlinks                                      │
│                                                             │
│  5. Archive                                                 │
│     - Move inbox file to processed/                         │
│     - Log activity to Google Sheets                         │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   MAINTENANCE & MONITORING                 │
├─────────────────────────────────────────────────────────────┤
│  • Gap Finder (Daily)      → Find missing WikiLinks         │
│  • Error Handler           → Retry + review queue           │
│  • Activity Logging        → Google Sheets audit trail      │
└─────────────────────────────────────────────────────────────┘
```

---

## Workflows

### 1. Auto-Learning Engine (`clawmind-auto-learning.json`)
**Trigger:** Every 15 minutes (or manual)
**Purpose:** Process inbox files and integrate into knowledge graph

**What it does:**
- Scans `~/ClawMind/inbox/*.md`
- Extracts metadata, WikiLinks, topics
- Checks for duplicates
- Creates or updates notes
- Updates Index.md with new stats
- Moves processed files to `inbox/processed/`
- Logs activity

---

### 2. Conversation Capture (`clawmind-conversation-capture.json`)
**Trigger:** Webhook (`/webhook/clawmind-conversation`)
**Purpose:** Capture conversations for later processing

**What it does:**
- Accepts POST with conversation data
- Formats as Obsidian note
- Writes to inbox
- Triggers auto-learning
- Returns success/failure

**API Format:**
```json
POST http://localhost:5678/webhook/clawmind-conversation
{
  "content": "Full conversation text...",
  "title": "Session with Jakin about X",
  "source": "webchat",
  "tags": ["flybrain", "neuroscience"],
  "summary": "Key points discussed...",
  "insights": ["Insight 1", "Insight 2"],
  "links": ["FlyBrainAI", "Consciousness"],
  "duration": "45 minutes"
}
```

---

### 3. Gap Finder (`clawmind-gap-finder.json`)
**Trigger:** Daily at midnight (Chicago time)
**Purpose:** Find broken WikiLinks in knowledge graph

**What it does:**
- Scans all notes for WikiLinks
- Compares against existing files
- Generates report of missing connections
- Saves to `~/ClawMind/reports/knowledge-gaps-YYYY-MM-DD.md`
- Alerts if >10 missing links

---

### 4. Error Handler (`clawmind-error-handler.json`)
**Trigger:** Any workflow failure
**Purpose:** Handle errors gracefully

**What it does:**
- Captures error details
- Logs to Google Sheets review queue
- Sends Telegram alert
- Retries network errors after 5 minutes
- Escalates critical errors

---

## Directory Structure

```
~/ClawMind/
├── inbox/
│   ├── *.md                    # New content waiting to be processed
│   └── processed/              # Archived after processing
├── reports/
│   └── knowledge-gaps-*.md     # Daily gap analysis reports
├── learning-queue/             # For complex multi-step learning
├── *.md                        # Your knowledge graph notes
└── Index.md                    # Auto-updated dashboard

~/n8n-workflows/
├── clawmind-auto-learning.json
├── clawmind-conversation-capture.json
├── clawmind-gap-finder.json
├── clawmind-error-handler.json
└── config.md
```

---

## Environment Variables Required

Add these to your `.env` file or n8n credentials:

```bash
# Telegram (for alerts)
TELEGRAM_CHAT_ID=your_chat_id
TELEGRAM_BOT_TOKEN=your_bot_token

# Google Sheets (for logging)
CLAWMIND_LOG_SHEET_ID=your_sheet_id

# Optional: For notifications
ADMIN_EMAIL=your@email.com
```

---

## Activation Steps

### 1. Install n8n

**Option A: npm**
```bash
npm install n8n -g
```

**Option B: Docker**
```bash
docker run -it --rm \
  --name n8n \
  -p 5678:5678 \
  -v ~/.n8n:/home/node/.n8n \
  -v ~/n8n-workflows:/backup \
  -e TELEGRAM_CHAT_ID=your_id \
  -e CLAWMIND_LOG_SHEET_ID=your_sheet \
  n8nio/n8n
```

### 2. Start n8n
```bash
n8n start
# or
open http://localhost:5678
```

### 3. Import Workflows

1. Open n8n web UI: http://localhost:5678
2. Click "Workflows" → "Import from File"
3. Import each workflow from `~/n8n-workflows/clawmind-*.json`
4. Set credentials for:
   - Telegram (optional)
   - Google Sheets (optional)
   - Any other integrations

### 4. Activate Workflows

| Workflow | Recommended Status |
|----------|-------------------|
| Auto-Learning Engine | ✅ Active |
| Conversation Capture | ✅ Active |
| Gap Finder | ✅ Active |
| Error Handler | ✅ Active (already set) |

### 5. Test

**Test auto-learning:**
```bash
echo "# Test Note\n\nThis is a [[Test]] note." > ~/ClawMind/inbox/test-note.md
# Wait 15 minutes or trigger manually
```

**Test conversation capture:**
```bash
curl -X POST http://localhost:5678/webhook/clawmind-conversation \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Test conversation content",
    "title": "Test Session",
    "source": "test"
  }'
```

---

## Usage Patterns

### Pattern 1: Auto-Capture Conversations
When we finish a significant conversation, I'll call the webhook:
```javascript
// Automatically done at 78% tokens or end of session
fetch('http://localhost:5678/webhook/clawmind-conversation', {
  method: 'POST',
  body: JSON.stringify({
    content: conversationText,
    title: 'Session about X',
    insights: extractedInsights,
    links: mentionedTopics
  })
});
```

### Pattern 2: Manual Knowledge Dump
Drop a markdown file into `~/ClawMind/inbox/`:
```markdown
---
tags: [concept, ai]
---

# New Concept I Learned

Key points...

Related: [[Existing Note]]
```

### Pattern 3: Web Research
Use the multi-search skill, save results to inbox:
```bash
echo "# Research: Topic\n\n$(search_results)" > ~/ClawMind/inbox/research-topic.md
```

---

## Monitoring

### Google Sheets Log
Track all learning activity:
- Timestamp
- Action (created/updated/skipped)
- Note name
- Type
- Word count
- Links found

### Telegram Alerts
Get notified for:
- Critical errors
- High missing link counts (>10)
- Daily digest (optional)

### Reports
Review daily in `~/ClawMind/reports/`:
- Knowledge gap analysis
- Missing WikiLinks
- Recommendations

---

## Maintenance

### Weekly
- Review `inbox/processed/` (cleanup old files)
- Check reports for patterns
- Update this config if needed

### Monthly
- Archive old reports
- Review error logs
- Tune processing rules

### As Needed
- Add new input sources
- Modify extraction logic
- Update classification rules

---

## Customization

### Add New Note Types
Edit `clawmind-auto-learning.json` → "Extract Metadata" node:
```javascript
// Add to noteType logic
} else if (content.includes('# Tool') || metadata.tags?.includes('tool')) {
  noteType = 'tool';
}
```

### Change Processing Frequency
Edit trigger node in auto-learning:
- Currently: 15 minutes
- Options: Manual, Webhook, Cron schedule

### Add New Outputs
Add nodes after "Log Activity":
- Send to Notion
- Post to Slack
- Update database

---

## Troubleshooting

### Inbox files not processing
- Check n8n is running: `curl http://localhost:5678/healthz`
- Verify workflow is active
- Check error handler logs

### Duplicate notes created
- Deduplication uses note title/topic
- Check existing notes for similar names
- Review `corrections.md` for pattern adjustments

### WikiLinks not extracting
- Format must be: `[[Target]]` or `[[Target|Display]]`
- Check regex in "Extract Metadata" node
- Verify no special characters breaking parsing

---

## Integration with Self-Improving

The auto-learning engine feeds into self-improving:

1. **New patterns discovered** → Logged to `~/self-improving/projects/clawmind.md`
2. **Errors encountered** → Logged to `corrections.md`
3. **User corrections** → Used to tune extraction/classification

Example: If you correct "That's not how I want topics classified," I log it and update the classifier.

---

## Future Enhancements

### Planned
- [ ] Vector embedding for semantic search
- [ ] Automatic topic clustering
- [ ] AI-generated summaries
- [ ] Cross-reference suggestions
- [ ] Knowledge gap prediction

### Ideas
- [ ] Import from Readwise
- [ ] Kindle highlights → Notes
- [ ] Podcast transcript processing
- [ ] Meeting recording transcription
- [ ] Browser bookmark archiving

---

## Status

| Component | Status |
|-----------|--------|
| Directory structure | ✅ Created |
| Workflow files | ✅ Generated |
| Error handling | ✅ Configured |
| Documentation | ✅ Complete |
| n8n activation | ⏳ Pending |
| Telegram setup | ⏳ Optional |
| Google Sheets | ⏳ Optional |

---

**Ready to activate? Run:**
```bash
n8n start
# Then import workflows at http://localhost:5678
```

---

*Your ClawMind now learns continuously. Never miss an insight. Never lose a connection.*
