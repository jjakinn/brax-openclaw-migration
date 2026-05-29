# n8n Workflow Automation — Configuration

## Active Workflows

| Workflow | Trigger | Status | Purpose |
|----------|---------|--------|---------|
| Token Monitor | Cron (30min) | Ready | Alert at 75% tokens |
| Error Handler | On Error | Active | Route failures to queue |
| Daily Digest | Daily | Ready | Metrics email |
| **ClawMind Auto-Learning** | Cron (15min) | Ready | Process knowledge inbox |
| **ClawMind Conversation** | Webhook | Ready | Capture sessions |
| **ClawMind Gap Finder** | Daily | Ready | Find broken WikiLinks |
| **ClawMind Error Handler** | On Error | Active | ClawMind-specific errors |

## ClawMind Integration

See `CLAWMIND-README.md` for complete documentation.

**Quick Start:**
```bash
# Check status
~/ClawMind/clawmind.sh status

# Submit content
echo "# New Note" | ~/ClawMind/clawmind.sh submit "My Note"

# Manual process
curl -X POST http://localhost:5678/webhook/clawmind-process
```

**Directory Structure:**
```
~/ClawMind/
├── inbox/           # Drop files here to auto-process
├── inbox/processed/ # Archived after processing
├── reports/         # Gap analysis reports
└── *.md            # Your knowledge graph
```

### Standard Pattern
1. **Trigger** — Cron / Webhook / Manual
2. **Validate** — Check inputs
3. **Process** — Main logic
4. **Log** — Audit trail
5. **Error Handling** — Retry + review queue
6. **Notify** — Success/failure alerts

## Design Principles

### Idempotency
- Use deduplication keys
- Check before creating
- Handle re-runs safely

### Error Handling
- Per-node error branches
- Exponential backoff retry
- Final failure → review queue
- Never silent failures

### Observability
- `run_id` for every execution
- Start/end timestamps
- Status tracking
- Error details logged

## Human-in-the-Loop

Failures go to review queue:
- Google Sheet or database
- Human approves/rejects
- Approved items reprocess
- Rejected items archived

## Credentials

Stored in n8n credential manager:
- API keys (never in workflow JSON)
- OAuth tokens
- Database connections

## Backup

Workflows versioned in:
- `~/n8n-workflows/backup/`
- Git repository (optional)

---

*Configure n8n instance at: http://localhost:5678 (when running)*
