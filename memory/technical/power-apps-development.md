### ⚡ Power Apps Code Apps - Development Workflow
- **Learned:** March 31, 2026
- **Video Reference:** https://www.youtube.com/watch?v=UBFgFNYbSTA (Raza's Code Apps tutorial)
- **Project Example:** Texan Title Insurance Calculator (`~/Desktop/texan-title-calculator/`)

**Complete Workflow:**
```bash
# 1. Create React app
npm create vite@latest my-app -- --template react-ts
cd my-app && npm install

# 2. CRITICAL: Set relative base path in vite.config.ts for Power Apps:
export default defineConfig({
  base: './',  // ← REQUIRED for Power Apps!
  plugins: [react()],
})

# 3. Build for production
npm run build  # Creates /dist folder with ./assets/ paths (not /assets/)

# 4. Configure .NET for Power Platform CLI
export PATH="$HOME/.dotnet:$PATH"
export DOTNET_ROOT="$HOME/.dotnet"

# 5. Initialize as Code App
~/pac-cli/pac-osx/tools/pac.sh code init -n "AppName" -b ./dist -f index.html

# 6. Deploy to Power Platform
~/pac-cli/pac-osx/tools/pac.sh code push
```

**⚠️ CRITICAL FIX - White Screen Issue:**
Power Apps serves from a subdirectory, so you MUST use relative paths:
- ❌ BAD: `/assets/index.js` (absolute)
- ✅ GOOD: `./assets/index.js` (relative)

Without `base: './'` in vite.config.ts, the app shows a white screen in Power Apps because it can't find the assets.

**Key Commands:**
| Command | Purpose |
|---------|---------|
| `pac auth create` | Authenticate |
| `pac env list` | Show environments |
| `pac env select --environment <url>` | Switch env |
| `pac code init -n <name> -b <build> -f <entry>` | Initialize |
| `pac code push` | Deploy |

**Prerequisites:**
- Enable "Code apps" in Power Platform Admin Center first
- Wait 10-20 min after enabling for provisioning
- Requires .NET 10+ (arm64 for Apple Silicon)

**Local Testing:**
```bash
cd ~/Desktop/my-app
npm run dev  # http://localhost:3000
```

**Troubleshooting:**
- 403 error = Code Apps not enabled (ask admin)
- DNS error = Still provisioning (wait 15 min)
- ENOTFOUND = Environment reconfiguring after enable

**⚠️ CRITICAL FIX - Images/Logos Not Showing (Question Mark):**
When embedding images as base64 data URIs in Power Apps Code Apps, you MUST include the **COMPLETE** base64 string, not truncated:

```typescript
// ❌ BAD - Truncated (shows broken image/question mark)
const LOGO = "data:image/jpeg;base64,/9j/4AAQ...truncated...";

// ✅ GOOD - Complete base64 (image displays correctly)
const LOGO = "data:image/jpeg;base64,/9j/4AAQ...[FULL 8KB+ DATA]...";
```

**Generate complete base64:**
```bash
# Resize image first (keep under 20KB)
sips -Z 100 logo.jpg --out logo-small.jpg

# Generate base64
base64 -i logo-small.jpg

# Copy ENTIRE output into your React code
```

**Why:** Power Apps Code Apps don't support external image URLs due to security, but embedded data URIs work perfectly IF complete.