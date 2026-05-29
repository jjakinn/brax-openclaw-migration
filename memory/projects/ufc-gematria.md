### 🥊 UFC Gematria v3 — Ultimate Deep Analysis (Active - Running on localhost:3000)
- **Concept:** Multi-layered UFC fight prediction combining Jewish numerology, English gematria, real-time fight stats, camp intelligence, and narrative context
- **Stack:** Next.js 16 + React 19 + TypeScript + Tailwind CSS v4 + SQLite (`better-sqlite3`)
- **Location:** `~/.openclaw/workspace/ufc-gematria/`
- **Running at:** http://localhost:3000
- **Status:** Production-ready. 10 integrated analysis sections.

**The 10 Analysis Layers:**
1. **Core Gematria Ties** — EO + RO cross-matches (fighter names, nicknames, event)
2. **Direct Script Number Alignments** — exhaustive Jesuit/Black Pope/Pope Francis/Robert Francis Prevost mappings across all 10 ciphers
3. **Fight Date Codes** — numeric reductions, IED distances to papal/Jesuit anniversaries, prime mappings
4. **Record & Outcome Forks** — win/loss/draw scenarios with gematria hits and nth-prime ties (15th prime=47, 43rd prime=191 = Society of Jesus, 56th prime=263 = Robert Francis Prevost)
5. **Fight Importance & Narrative Context** — title fight, main event, co-main, retirement, comeback, debut, final contract flags
6. **Age & Experience Gap** — exact ages on fight date with narrative rules (young prospect vs veteran when gap ≥5 years and one ≥35)
7. **Fight Camp Intel** — RSS feeds (MMAFighting, BloodyElbow, ESPN, UFC, MMAWeekly, Yahoo Sports), Sherdog scrape, DuckDuckGo search; keyword flags for injury/strong camp/poor camp/weight issues/coach drama/new training partners
8. **Fight Stats & Specialties** — career averages + stance-specific stats from UFC-DataLab CSVs via SQLite (`ufc_stats.db`: 4,477 fighters, 8,624 fights, 40,570 round-by-round stats, 2,662 profiles)
9. **Side-by-Side Script Comparison** — weighted composite scoring:
   - Gematria direct hits = **3x**
   - Historical stats = **2x**
   - Camp intel flags = **1.5x**
   - Importance/Age narrative = **1x**
10. **Script Prediction & Probability** — cites dominant layers across all categories with moneyline-style call

**Data Infrastructure:**
- SQLite DB: `data/ufc_stats.db`
- Import script: `scripts/import-ufc-data.ts`
- Profile builder: `scripts/build-fighter-profiles.ts`
- Auto-update: `scripts/update-ufc-stats.sh`

**Event Fallback Fix (2026-04-11):**
- ESPN stopped returning upcoming events immediately after UFC 327 ended
- Built `/api/ufc-events` server-side cheerio scraper that fetches the **next upcoming card only** from UFC.com
- Returns **all fights on that single card**
- Current result: **UFC Fight Night — Burns vs Malott (April 18, 2026)** with 10 bouts

**UI Fixes:**
- **Extended Gematria toggle** — backend uses `getActiveCiphers(useExtended)`; raw gematria panel hides extended badges when OFF
- **Full Analysis toggle** — compacts from ~72 blocks to ~32 blocks; shows "Showing X of Y blocks" badge

**Key API Routes:**
- `/api/gematria?text=` — gematria calculator (10 ciphers)
- `/api/fighter-stats?a=&b=` — DB lookup for career/stance-specific stats
- `/api/camp-intel?a=&b=` — aggregated camp intelligence
- `/api/ufc-events` — UFC.com fallback scraper for next card
- `/api/tapology?name=` — Tapology proxy (currently broken due to upstream HTML changes)
- `/api/sherdog?name=` — Sherdog scraper (currently broken, returns garbage data)