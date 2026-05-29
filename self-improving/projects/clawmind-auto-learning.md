# Project: ClawMind Auto-Learning

## Description
n8n automation system that continuously learns and updates my Obsidian knowledge graph.

## Key Patterns

### Automated Knowledge Capture
- **Trigger:** Webhook, file drop, or schedule
- **Process:** Extract → Deduplicate → Route → Update Index
- **Output:** Structured notes in knowledge graph

### Conversation Integration
- Capture at 78% tokens (checkpoint)
- Capture at end of significant sessions
- Auto-extract insights and WikiLinks

### Maintenance
- Daily gap analysis (find broken links)
- Error handling with review queues
- Activity logging for audit trail

## User Preferences
- **Processing frequency:** Every 15 minutes
- **Deduplication:** Check by title/topic
- **Notification:** Telegram for critical only
- **Review queue:** Google Sheets

## Integration Points

### From ClawMind
- Reads: `inbox/*.md`
- Writes: `*.md`, `Index.md`, `reports/*.md`
- Archives: `inbox/processed/`

### From Self-Improving
- Logs patterns to `projects/clawmind.md`
- Uses corrections to tune extraction
- Feeds insights to HOT memory

### From n8n
- Webhook triggers for real-time capture
- Scheduled jobs for maintenance
- Error workflows for resilience

## Workflows

| Workflow | File | Purpose |
|----------|------|---------|
| Auto-Learning | `clawmind-auto-learning.json` | Process inbox files |
| Conversation | `clawmind-conversation-capture.json` | Capture sessions |
| Gap Finder | `clawmind-gap-finder.json` | Find broken links |
| Error Handler | `clawmind-error-handler.json` | Handle failures |

## CLI Tool
`~/ClawMind/clawmind.sh` - Quick commands:
- `status` - System status
- `process` - Manual trigger
- `submit` - Add to inbox
- `gaps` - Run analysis

## Related
- [[ClawMind]] - The knowledge graph
- [[Super Agent Configuration]] - Overall setup
- [[n8n]] - Automation platform
