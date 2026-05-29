# Recent Corrections

## 2026-04-08 — Broke Gateway Config During Telegram Setup

**What happened:**
- Attempting to set up Telegram integration
- Claw modified a `.json` configuration file directly
- Gateway failed to open entirely (wouldn't start)
- Jakin had to manually fix the configuration

**Root cause:**
- Directly edited JSON config without validation or backup
- Unknown: which specific file was modified (likely `openclaw.json` or gateway config)

**Prevention:**
- Never modify system/config files without explicit instruction
- When in doubt, ASK before changing anything infrastructure-related
- Test changes in isolated environment first
- Keep backups before any config modifications

**Status:** Fixed by Jakin
