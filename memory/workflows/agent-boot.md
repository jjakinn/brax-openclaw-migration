# AGENT-BOOT.md - Session Startup Protocol

**READ THIS FIRST** before doing anything else.

## ⚠️ CHECKPOINT RECOVERY PROTOCOL

### Step 1: Check for Active Tasks
Read `memory/workflows/task-queue.md`

**If tasks exist:**
- Load the HIGHEST PRIORITY incomplete task
- Read its checkpoint file from `memory/workflows/checkpoints/`
- Continue EXACTLY where the previous session left off
- Do NOT start new tasks until the queue is cleared

**If queue is empty:**
- Proceed with normal operations
- Read `MEMORY.md` and other context files as usual

### Step 2: Token Monitoring (Ongoing)
While working on any large task:
- Check token usage periodically
- At 78% usage (~204k tokens), CREATE CHECKPOINT immediately
- Save progress to `memory/workflows/checkpoints/task-{timestamp}.md`
- Update `task-queue.md` with status: `paused`
- **SPAWN CONTINUATION AGENT automatically** to resume work
- Halt current session

### Step 3: Task Completion
When a task finishes:
- Update `task-queue.md` (mark complete, remove from active)
- Archive checkpoint file to `memory/workflows/checkpoints/archive/`

---

## Quick Reference

| Token Usage | Action |
|-------------|--------|
| 0-50% | Work normally |
| 50-75% | Work normally, be aware |
| 78%+ | **STOP & CHECKPOINT** |
| 85%+ | **EMERGENCY: Save & Halt** |

## Checkpoint File Format
See: `memory/workflows/checkpoint-template.md`
