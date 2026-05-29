# CHECKPOINT TEMPLATE

**Use this format when creating a checkpoint at 78% token usage.**

```markdown
# CHECKPOINT - {TIMESTAMP}

## Task Identification
- **Task ID:** task-{number}
- **Task Name:** {brief description}
- **Created At:** YYYY-MM-DD HH:MM:SS
- **Checkpoint Reason:** Token limit reached (78%+)

## Original Instructions
> Paste the original task instructions here verbatim

## Current Progress
- **Overall Completion:** X%
- **Current Step:** {what was being done}
- **Next Step:** {what needs to be done next}

## Files/Artifacts Created
- `path/to/file-1.md` - {description}
- `path/to/file-2.md` - {description}

## Intermediate State
If processing data, note the last processed item:
- Last timestamp: HH:MM:SS
- Last page: X
- Last ID: {identifier}
- Last processed line: "{content snippet}"

## Context & Dependencies
- **Prerequisites met:** Yes/No - which ones
- **Blocked by:** Any dependencies
- **Required for:** What this unlocks

## Token Usage at Checkpoint
- **Tokens Used:** ~{number}
- **Estimated Remaining for Task:** ~{number} tokens
- **Recommendation:** Continue in new session (`openclaw tui --session "$(date +%s)"`)

## Resume Instructions for Next Agent
1. Load {specific files}
2. Resume from {specific position}
3. Continue with {specific action}
4. Next checkpoint should be at {position}

## Auto-Continuation Command
When this checkpoint is created, spawn continuation agent with:
```
Task: "Read memory/workflows/task-queue.md, find the highest priority paused task, read its checkpoint file from memory/workflows/checkpoints/task-{timestamp}.md, and continue EXACTLY where the previous agent left off. Do not ask the user what to do - just continue the work from the checkpoint."
```

## Notes for Resumption
[Any important context, partial thoughts, or warnings]
```

---

## How to Use

1. At 78% token usage, copy this template
2. Fill in ALL fields
3. Save to `checkpoints/task-{timestamp}.md`
4. Update `task-queue.md` with status: `paused`
5. New agent reads checkpoint and continues
