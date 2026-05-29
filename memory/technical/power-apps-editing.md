### Power Apps Code Apps — Editing Workflow

**Title Insurance Calculator:**
| Environment | App Name | App ID | Config File | Status |
|-------------|----------|--------|-------------|--------|
| IT Help Desk | TexanTitleCalculator | `cc5584ba-798a-4479-a445-fc8d260304b5` | `power.config.json.IT-HelpDesk` | ✅ Live |
| Texan Title (default) | TexanTitleCalculator | `4ec28b04-72e6-4f9e-b8ca-48e05aa3a03a` | `power.config.json` (active) | ✅ Live |
| TTH Dev | TitleCalculator-TTHDev | `db0a1688-45d1-41a4-a1fa-4fe5ad0dca05` | `power.config.json.TTH-Dev` | ✅ Live |

**Net Sheet Calculator:**
| Environment | App Name | App ID | Config File | Status |
|-------------|----------|--------|-------------|--------|
| IT Help Desk | NetSheetCalculator | `e5691088-a163-451a-9cb6-d0d2d314e122` | `power.config.json.IT-HelpDesk-NetSheet` | ✅ Live |
| TTH Dev | NetSheetCalculator | `3d73caae-9cfc-42f4-8b21-a02cc8cb950d` | `power.config.json.TTH-Dev-NetSheet` | ✅ Live |

**Project Locations:**
- Title Insurance: `~/Desktop/texan-title-calculator/`
- Net Sheet: `~/Desktop/texan-net-sheet-calculator/`

**⚠️ CRITICAL — Tailwind CSS v4 Setup:**
When creating new Vite + React + Tailwind projects, use this exact `src/index.css`:
```css
@import "tailwindcss";

@theme {
  --color-texan-50: #f0f9ff;
  --color-texan-100: #e0f2fe;
  --color-texan-600: #0284c7;
  --color-texan-700: #0369a1;
}

@layer base {
  * { border-color: var(--color-slate-200, #e2e8f0); }
  body { background-color: #f8fafc; color: #0f172a; }
}
```
**DO NOT use `@tailwind base/components/utilities` — this is v3 syntax and breaks styling in v4.**
| **TTH Dev** | **NetSheetCalculator** | `3d73caae-9cfc-42f4-8b21-a02cc8cb950d` | `power.config.json.TTH-Dev-NetSheet` | ✅ **Live** |

**⚠️ IMPORTANT — Two TTH Dev Environments Exist:**
| Environment | URL | Environment ID | Status |
|-------------|-----|----------------|--------|
| ✅ **TTH Dev (correct)** | `https://orgecde1220.crm.dynamics.com/` | `0c5fcc5f-6cb2-e1c8-9f3f-c0da2f075e01` | ✅ Code Apps enabled, permissions work |
| ❌ TTH DEV (wrong) | `https://tthcrm-dev.crm.dynamics.com/` | `7b533325-66c9-e15c-98c0-21efe209f805` | ❌ 403 — Code Apps not enabled or permissions missing |

**Always use `https://orgecde1220.crm.dynamics.com/` for TTH Dev deployments.**

**Project Location:** `~/Desktop/texan-title-calculator/`

**Edit → Build → Deploy Workflow:**
```bash
# 1. Edit React/TypeScript code in src/
cd ~/Desktop/texan-title-calculator

# 2. Build for production
npm run build

# 3. Configure .NET for Power Platform CLI
export PATH="$HOME/.dotnet:$PATH"
export DOTNET_ROOT="$HOME/.dotnet"

# 4. Push to current environment (reads power.config.json)
~/pac-cli/pac-osx/tools/pac.sh code push
```

**Switch Between Environments:**
```bash
cd ~/Desktop/texan-title-calculator

# Switch to IT Help Desk
mv power.config.json power.config.json.TexanTitle
mv power.config.json.IT-HelpDesk power.config.json
~/pac-cli/pac-osx/tools/pac.sh env select --environment "https://tthelpdesk.crm.dynamics.com/"

# Switch to Texan Title (default)
mv power.config.json power.config.json.IT-HelpDesk
mv power.config.json.TexanTitle power.config.json
~/pac-cli/pac-osx/tools/pac.sh env select --environment "https://org41433bc8.crm.dynamics.com/"

# Switch to TTH Dev (CORRECT — use orgecde1220, NOT tthcrm-dev)
mv power.config.json power.config.json.TexanTitle
mv power.config.json.TTH-Dev power.config.json
~/pac-cli/pac-osx/tools/pac.sh env select --environment "https://orgecde1220.crm.dynamics.com/"
```

**Key Files Edited:**
- `src/components/App.tsx` — Main app shell with tabs
- `src/components/QuickQuoteForm.tsx` — Quick quote input form
- `src/components/CalculatorForm.tsx` — Advanced calculator form
- `src/components/ResultsDisplay.tsx` — Quote results display
- `src/engine/calculator.ts` — Calculation engine + validation
- `vite.config.ts` — Build config (must have `base: './'` for Power Apps)

**⚠️ Critical Requirements:**
- `vite.config.ts` must have `base: './'` (relative paths, not absolute)
- Power Apps blocks external images — use base64 data URIs
- Validation engine requires `loanAmount` only for Lender/Simultaneous policies
- Each environment needs separate `power.config.json` (app ID is environment-specific)
**Version:** 2.4.1+g3799f3e (.NET 10.0.5)  
**Location:** `~/pac-cli/pac-osx/tools/pac.sh` (aliased as `pac`)

**Core Commands:**
| Command | Purpose |
|---------|---------|
| `pac auth create` | Authenticate to Power Platform (interactive) |
| `pac auth list` | List authentication profiles |
| `pac auth select` | Switch between profiles |
| `pac canvas list` | List all canvas apps |
| `pac canvas create --msapp <name>` | Create new canvas app |
| `pac canvas pack --sources <dir> --msapp <name>` | Pack source to .msapp |
| `pac canvas unpack --msapp <name> --sources <dir>` | Unpack .msapp to source |
| `pac solution create --name <name>` | Create new solution |
| `pac solution export --name <name>` | Export solution |
| `pac env list` | List Dataverse environments |
| `pac data table list` | List Dataverse tables |
| `pac pcf init` | Create PCF component |
| `pac admin` | Admin account operations |
| `pac application` | Dataverse marketplace apps |
| `pac catalog` | Power Platform Catalog |
| `pac code` | Code apps (Preview) |
| `pac connection` | Dataverse connections |
| `pac connector` | Custom connectors |
| `pac copilot` | Copilot management |
| `pac managed-identity` | Managed Identity records |
| `pac model` | Model-driven apps (Preview) |
| `pac modelbuilder` | Dataverse API/Table generator |
| `pac package` | Dataverse package projects |
| `pac pages` | Power Pages website |
| `pac pipeline` | Pipeline operations |
| `pac plugin` | Dataverse plug-ins |
| `pac power-fx` | Power Fx commands (Preview) |
| `pac telemetry` | Telemetry settings |
| `pac test` | Automated Power App tests (Preview) |
| `pac tool` | Installable Power Platform tools |

---