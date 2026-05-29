# 🦾 BRAX OPENCLAW MIGRATION — WINDOWS ONE-COMMAND SETUP

**Date:** 2026-05-29
**OpenClaw Version:** 2026.3.2 (LOCKED)
**Platform:** Windows 10/11 (x64)
**Based on:** Jakin's exact macOS setup, ported to Windows

---

## ⚡ THE ONE COMMAND (After you have the files)

### Method 1: Right-click → Run (Easiest)
1. Extract `brax-openclaw-migration.zip` anywhere (Desktop, Downloads, etc.)
2. Open the `brax-migration` folder
3. **Right-click `RUN-ME-FIRST.ps1` → "Run with PowerShell"**
4. Done — everything installs automatically

### Method 2: Copy-Paste One Command (PowerShell)
If you extracted the zip to `C:\Users\Brax\Downloads\brax-migration`:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; cd "$env:USERPROFILE\Downloads\brax-migration"; .\RUN-ME-FIRST.ps1
```

Or if you extracted to Desktop:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force; cd "$env:USERPROFILE\Desktop\brax-migration"; .\RUN-ME-FIRST.ps1
```

---

## 📦 What's In The ZIP

| File | Purpose |
|------|---------|
| `RUN-ME-FIRST.ps1` | **The one script you run** — installs Node.js, OpenClaw, copies all configs |
| `setup-windows.ps1` | Full setup logic (called by RUN-ME-FIRST) |
| `workspace-files/` | 9 core .md files (MEMORY, SOUL, USER, etc.) |
| `skills/` | 80 OpenClaw skills |
| `memory/` | 50+ daily memory logs |
| `n8n-workflows/` | 11 n8n workflow files |
| `self-improving/` | Learning system (HOT/WARM/COLD memory) |
| `data-analysis/` | Analysis config |
| `MANIFEST.md` | Complete inventory |
| `INVENTORY.md` | Full system catalog |
| `README.md` | Setup guide |

---

## 🚀 What Happens When You Run It

1. **Checks for Node.js** — installs it automatically if missing (downloads + silent install)
2. **Installs OpenClaw 2026.3.2** — exact same version as Jakin
3. **Creates all directories** — workspace, memory, skills, self-improving, n8n, data-analysis
4. **Copies all files** — workspace configs, 80 skills, 50 memory archives, n8n workflows
5. **Generates openclaw.json** — with Windows paths, your name, random gateway token
6. **Substitutes names** — Jakin → Brax everywhere
7. **Updates paths** — macOS paths → Windows paths
8. **Verifies everything** — checks all components are in place
9. **Tells you the ONE thing left** — adding your Kimi API key

**Takes about 5-10 minutes total** (mostly Node.js install if you don't have it).

---

## 🔑 After Setup: The ONE Thing You Configure

```powershell
openclaw auth add kimi-coding
```

Paste your Kimi API key when prompted.

**Get your key:** https://platform.moonshot.cn

---

## 🌐 Optional: Brave Search API Key

For web search to work:
1. Get free key: https://api.search.brave.com/app/dashboard
2. Edit: `%USERPROFILE%\.openclaw\openclaw.json`
3. Find: `YOUR_BRAVE_API_KEY_HERE`
4. Replace with your key

---

## 🚀 Start OpenClaw

```powershell
openclaw gateway start
```

Then open: http://localhost:18789

---

## ✅ What's Identical to Jakin

- **OpenClaw version:** 2026.3.2 (exact)
- **Workspace files:** MEMORY, SOUL, USER, HEARTBEAT, AGENTS, TOOLS — all content identical
- **80 skills:** Same skill files, same configurations
- **50 memory archives:** Every daily log from Jakin's system
- **Super Agent Mode:** GitNexus, n8n, data-analysis, self-improving protocols
- **Kimi model:** k2p5 primary + fallbacks

## 🔀 What's Different (On Purpose)

| | Jakin (macOS) | Brax (Windows) |
|---|---|---|
| Name | Jakin | Brax (auto-substituted) |
| OS | macOS | Windows 10/11 |
| Paths | `/Users/Jakin/...` | `C:\Users\Brax\...` |
| Shell | zsh | PowerShell |
| Telegram | Enabled | **Disabled** (webchat only) |
| Node.js | Homebrew | MSI installer (auto) |
| Brew tools | 150 formulas | Not applicable |
| Ollama | Homebrew | Separate install (optional) |

---

## 🆘 Troubleshooting

### "ExecutionPolicy" error
Run PowerShell as Administrator, then:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then re-run the setup.

### "Node.js not found" even after install
Close and reopen PowerShell, then try again. The PATH needs to refresh.

### "npm not found"
Same as above — restart PowerShell after Node.js installs.

### Something else broke
The script creates a log file. Check:
```
%TEMP%\brax-openclaw-setup.log
```

---

## 📞 Need Help?

Contact Jakin — he built this exact setup and knows every detail.

**Built with 💀 by Jakin for Brax**
**OpenClaw 2026.3.2 — Exact Version Locked**
