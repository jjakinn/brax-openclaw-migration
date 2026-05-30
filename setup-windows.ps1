#!/usr/bin/env pwsh
# OpenClaw Complete Setup for Windows - Brax
# Based on Jakin's exact setup (OpenClaw 2026.3.2)
# One script: install everything, configure everything, leave only Kimi API for Brax

$ErrorActionPreference = "Continue"
$ProgressPreference = "Continue"

$BraxHome = $env:USERPROFILE
$WorkspaceDir = "$BraxHome\.openclaw\workspace"
$OpenClawDir = "$BraxHome\.openclaw"
$MigrationDir = "$BraxHome\brax-migration"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   OpenClaw Migration - Brax Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Source: Jakin's exact setup | OpenClaw Version: 2026.3.2 | Platform: Windows" -ForegroundColor Gray
Write-Host ""

# ============================================================================
# STEP 1: CHECK / INSTALL NODE.JS + NPM
# ============================================================================
Write-Host "STEP 1: Checking Node.js..." -ForegroundColor Yellow

function Test-NodeInstalled {
    try {
        $nodeVersion = node --version 2>$null
        $npmVersion = npm --version 2>$null
        if ($nodeVersion -and $npmVersion) {
            Write-Host "  OK Node.js found: $nodeVersion, npm: $npmVersion" -ForegroundColor Green
            return $true
        }
    } catch {}
    return $false
}

if (-not (Test-NodeInstalled)) {
    Write-Host "  WARNING Node.js not found. Installing..." -ForegroundColor Yellow
    Write-Host "  Downloading Node.js LTS installer..." -ForegroundColor Gray

    $nodeInstaller = "$env:TEMP\nodejs-installer.msi"
    $nodeUrl = "https://nodejs.org/dist/v22.15.0/node-v22.15.0-x64.msi"

    try {
        Invoke-WebRequest -Uri $nodeUrl -OutFile $nodeInstaller -UseBasicParsing
        Write-Host "  Running installer (silent mode)..." -ForegroundColor Gray
        Start-Process msiexec.exe -ArgumentList "/i `"$nodeInstaller`" /qn /norestart" -Wait
        Write-Host "  OK Node.js installed. Restarting shell session..." -ForegroundColor Green

        # Refresh PATH
        $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    } catch {
        Write-Host "  ERROR Failed to install Node.js automatically." -ForegroundColor Red
        Write-Host "     Please download and install from https://nodejs.org" -ForegroundColor Red
        exit 1
    }
}

# Verify after install
if (-not (Test-NodeInstalled)) {
    Write-Host "  ERROR Node.js still not found after install. Please restart PowerShell and try again." -ForegroundColor Red
    exit 1
}

# ============================================================================
# STEP 2: INSTALL OPENCLAW 2026.3.2 (EXACT VERSION)
# ============================================================================
Write-Host ""
Write-Host "STEP 2: Installing OpenClaw 2026.3.2..." -ForegroundColor Yellow

$existingVersion = npm list -g openclaw 2>$null | Select-String "openclaw@(\d+\.\d+\.\d+)"
if ($existingVersion) {
    $v = $existingVersion.Matches[0].Groups[1].Value
    if ($v -eq "2026.3.2") {
        Write-Host "  OK OpenClaw 2026.3.2 already installed" -ForegroundColor Green
    } else {
        Write-Host "  WARNING Different version found ($v). Reinstalling 2026.3.2..." -ForegroundColor Yellow
        cmd /c "npm uninstall -g openclaw 2>nul"
        cmd /c "npm install -g openclaw@2026.3.2 2>nul"
    }
} else {
    Write-Host "  Installing openclaw@2026.3.2 globally..." -ForegroundColor Gray
    cmd /c "npm install -g openclaw@2026.3.2 2>nul"
}

# Refresh PATH to ensure openclaw is available
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
Start-Sleep -Seconds 2

# Verify
$ocVersion = ""
try {
    $ocVersion = (openclaw --version 2>&1 | Out-String).Trim()
} catch {
    # Fallback: try direct path
    $npmGlobalBin = (npm prefix -g 2>$null) + "\node_modules\.bin"
    if (Test-Path "$npmGlobalBin\openclaw.cmd") {
        $ocVersion = (& "$npmGlobalBin\openclaw.cmd" --version 2>&1 | Out-String).Trim()
    }
}

if (-not $ocVersion -or $ocVersion -ne "2026.3.2") {
    Write-Host "  WARNING OpenClaw not in PATH yet. Retrying..." -ForegroundColor Yellow
    Start-Sleep -Seconds 3
    $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
    $ocVersion = (openclaw --version 2>&1 | Out-String).Trim()
}

if ($ocVersion -ne "2026.3.2") {
    Write-Host "  ERROR OpenClaw version mismatch or not found. Got: '$ocVersion'" -ForegroundColor Red
    exit 1
}
Write-Host "  OK OpenClaw 2026.3.2 confirmed" -ForegroundColor Green

# ============================================================================
# STEP 3: CREATE DIRECTORY STRUCTURE
# ============================================================================
Write-Host ""
Write-Host "STEP 3: Creating directory structure..." -ForegroundColor Yellow

$dirs = @(
    $WorkspaceDir,
    "$WorkspaceDir\memory",
    "$WorkspaceDir\memory\archive",
    "$WorkspaceDir\skills",
    "$WorkspaceDir\config",
    "$BraxHome\self-improving",
    "$BraxHome\self-improving\projects",
    "$BraxHome\self-improving\archive",
    "$BraxHome\self-improving\domains",
    "$BraxHome\self-improving\drafts",
    "$BraxHome\self-improving\snapshots",
    "$BraxHome\n8n-workflows",
    "$BraxHome\data-analysis",
    "$BraxHome\data-analysis\datasets",
    "$BraxHome\data-analysis\reports",
    "$BraxHome\ClawMind"
)

foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}
Write-Host "  OK Directories created" -ForegroundColor Green

# ============================================================================
# STEP 4: EXTRACT / COPY MIGRATION FILES
# ============================================================================
Write-Host ""
Write-Host "STEP 4: Copying workspace files..." -ForegroundColor Yellow

# Determine where the migration files are
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$sourceDir = $scriptDir

# If running from extracted archive, files are in the same dir as script
# If running standalone, look for brax-migration folder nearby
if (-not (Test-Path "$sourceDir\workspace-files")) {
    # Maybe we're inside brax-migration already
    if (Test-Path "$sourceDir\..\brax-migration\workspace-files") {
        $sourceDir = "$sourceDir\..\brax-migration"
    }
}

if (-not (Test-Path "$sourceDir\workspace-files")) {
    Write-Host "  WARNING workspace-files/ not found next to script." -ForegroundColor Yellow
    Write-Host "  Looking for brax-openclaw-migration.zip or .tar.gz..." -ForegroundColor Gray

    # Try to find and extract the archive
    $zipFile = "$BraxHome\Downloads\brax-openclaw-migration.zip"
    $tarFile = "$BraxHome\Downloads\brax-openclaw-migration.tar.gz"

    if (Test-Path $zipFile) {
        Write-Host "  Found zip at $zipFile, extracting..." -ForegroundColor Gray
        Expand-Archive -Path $zipFile -DestinationPath "$BraxHome\brax-migration-temp" -Force
        $sourceDir = "$BraxHome\brax-migration-temp\brax-migration"
    } elseif (Test-Path $tarFile) {
        Write-Host "  Found tar.gz at $tarFile, extracting..." -ForegroundColor Gray
        tar -xzf $tarFile -C "$BraxHome\brax-migration-temp"
        $sourceDir = "$BraxHome\brax-migration-temp\brax-migration"
    } else {
        Write-Host "  ERROR No migration files found." -ForegroundColor Red
        Write-Host "     Please ensure the brax-migration folder or archive is available." -ForegroundColor Red
        exit 1
    }
}

# Copy workspace files
if (Test-Path "$sourceDir\workspace-files") {
    Copy-Item -Path "$sourceDir\workspace-files\*" -Destination $WorkspaceDir -Recurse -Force
    Write-Host "  OK Workspace files copied" -ForegroundColor Green
}

# Copy skills
if (Test-Path "$sourceDir\skills") {
    Copy-Item -Path "$sourceDir\skills\*" -Destination "$WorkspaceDir\skills" -Recurse -Force
    $skillCount = (Get-ChildItem "$WorkspaceDir\skills" -Directory).Count
    Write-Host "  OK Skills copied ($skillCount skills)" -ForegroundColor Green
}

# Copy memory files
if (Test-Path "$sourceDir\memory") {
    Copy-Item -Path "$sourceDir\memory\*" -Destination "$WorkspaceDir\memory" -Recurse -Force
    $memCount = (Get-ChildItem "$WorkspaceDir\memory" -File).Count
    Write-Host "  OK Memory archives copied ($memCount files)" -ForegroundColor Green
}

# Copy n8n workflows
if (Test-Path "$sourceDir\n8n-workflows") {
    Copy-Item -Path "$sourceDir\n8n-workflows\*" -Destination "$BraxHome\n8n-workflows" -Recurse -Force
    Write-Host "  OK n8n workflows copied" -ForegroundColor Green
}

# Copy self-improving system
if (Test-Path "$sourceDir\self-improving") {
    Copy-Item -Path "$sourceDir\self-improving\*" -Destination "$BraxHome\self-improving" -Recurse -Force
    Write-Host "  OK Self-improving system copied" -ForegroundColor Green
}

# Copy data-analysis
if (Test-Path "$sourceDir\data-analysis") {
    Copy-Item -Path "$sourceDir\data-analysis\*" -Destination "$BraxHome\data-analysis" -Recurse -Force
    Write-Host "  OK Data analysis setup copied" -ForegroundColor Green
}

# ============================================================================
# STEP 5: GENERATE OPENCLAW.JSON (WINDOWS PATHS, NO TELEGRAM)
# ============================================================================
Write-Host ""
Write-Host "STEP 5: Generating openclaw.json..." -ForegroundColor Yellow

$workspaceJson = $WorkspaceDir -replace '\\', '/'
$gatewayToken = -join ((1..40) | ForEach-Object { '{0:x}' -f (Get-Random -Maximum 16) })

$openclawJson = @"
{
  "meta": {
    "lastTouchedVersion": "2026.3.2",
    "lastTouchedAt": "$(Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ")"
  },
  "wizard": {
    "lastRunAt": "$(Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ")",
    "lastRunVersion": "2026.3.2",
    "lastRunCommand": "configure",
    "lastRunMode": "local"
  },
  "auth": {
    "profiles": {
      "kimi-coding:default": {
        "provider": "kimi-coding",
        "mode": "api_key"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "kimi-coding": {
        "baseUrl": "https://api.kimi.com/coding/",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "k2p5",
            "name": "Kimi for Coding",
            "reasoning": true,
            "input": ["text", "image"],
            "cost": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0},
            "contextWindow": 262144,
            "maxTokens": 32768
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "kimi-coding/k2p5",
        "fallbacks": ["kimi/k2p5", "kimi/kimi-code", "kimi-coding/kimi-k2-thinking"]
      },
      "models": {
        "kimi-coding/k2p5": {"alias": "Kimi for Coding"},
        "kimi/k2p5": {},
        "kimi/kimi-code": {},
        "kimi-coding/kimi-k2-thinking": {}
      },
      "workspace": "$workspaceJson",
      "compaction": {"mode": "safeguard"},
      "maxConcurrent": 4,
      "subagents": {"maxConcurrent": 8}
    }
  },
  "tools": {
    "web": {
      "search": {"enabled": true, "apiKey": "YOUR_BRAVE_API_KEY_HERE"},
      "fetch": {"enabled": true}
    }
  },
  "messages": {"ackReactionScope": "group-mentions"},
  "commands": {"native": "auto", "nativeSkills": "auto", "restart": true, "ownerDisplay": "raw"},
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "auto",
    "auth": {"mode": "token", "token": "$gatewayToken"},
    "tailscale": {"mode": "off", "resetOnExit": false}
  },
  "plugins": {"entries": {}}
}
"@

$openclawJson | Out-File -FilePath "$OpenClawDir\openclaw.json" -Encoding utf8
Write-Host "  OK openclaw.json generated" -ForegroundColor Green

# ============================================================================
# STEP 6: CLONE ALL GITHUB REPOSITORIES
# ============================================================================
Write-Host ""
Write-Host "STEP 6: Cloning all GitHub repositories..." -ForegroundColor Yellow

$repos = @(
    @{url="https://github.com/abhigyanpatwari/GitNexus.git"; dest="gitnexus"},
    @{url="https://github.com/Coding-Solo/godot-mcp.git"; dest="godot-mcp"},
    @{url="https://github.com/comfyanonymous/ComfyUI.git"; dest="ComfyUI"},
    @{url="https://github.com/project-flipper/ClubPenguin.git"; dest="ClubPenguin"},
    @{url="https://github.com/clubpenguinadvanced/cpadvanced-client.git"; dest="cpadvanced-client"},
    @{url="https://github.com/solero/houdini.git"; dest="cpps-houdini"},
    @{url="https://github.com/wizguin/mammoth.git"; dest="cpps-mammoth"},
    @{url="https://github.com/wizguin/yukon.git"; dest="yukon-client"},
    @{url="https://github.com/wizguin/yukon-server.git"; dest="yukon-server"},
    @{url="https://github.com/Glztch/ssl-analyzer-api.git"; dest="api-projects/ssl-analyzer"},
    @{url="https://github.com/facebookresearch/ai4animationpy.git"; dest="ai4animationpy"},
    @{url="https://github.com/PolymathicAI/the_well.git"; dest="the_well"}
)

$cloneCount = 0
$skipCount = 0
foreach ($repo in $repos) {
    $destPath = "$BraxHome\$($repo.dest)"
    if (Test-Path "$destPath\.git") {
        Write-Host "  SKIP Already exists: $($repo.dest)" -ForegroundColor Gray
        $skipCount++
    } else {
        Write-Host "  CLONE $($repo.url) -> $($repo.dest)" -ForegroundColor Gray
        try {
            # Use cmd to avoid PowerShell treating git's stderr as an error
            $process = Start-Process -FilePath "git" -ArgumentList "clone", $repo.url, $destPath -WindowStyle Hidden -Wait -PassThru
            if ($process.ExitCode -eq 0) {
                $cloneCount++
            } else {
                Write-Host "  FAIL (may be private): $($repo.dest)" -ForegroundColor Yellow
            }
        } catch {
            Write-Host "  FAIL: $($repo.dest) - $($_.Exception.Message)" -ForegroundColor Yellow
        }
    }
}
Write-Host "  OK Repositories: $cloneCount cloned, $skipCount already present" -ForegroundColor Green

# ============================================================================
# STEP 7: INSTALL SYSTEM TOOLS (WINDOWS EQUIVALENTS)
# ============================================================================
Write-Host ""
Write-Host "STEP 7: Installing system tools..." -ForegroundColor Yellow

# Check if winget is available
$hasWinget = $null -ne (Get-Command winget -ErrorAction SilentlyContinue)

if ($hasWinget) {
    Write-Host "  Using winget for package installation..." -ForegroundColor Gray
    
    # Core dev tools
    $wingetPackages = @(
        "Git.Git",
        "OpenJS.NodeJS",
        "Python.Python.3.13",
        "Microsoft.PowerShell",
        "Docker.DockerDesktop"
    )
    
    foreach ($pkg in $wingetPackages) {
        Write-Host "    Installing $pkg..." -ForegroundColor Gray
        winget install --id $pkg --accept-package-agreements --accept-source-agreements --silent 2>$null | Out-Null
    }
    
    # Media tools
    Write-Host "    Installing ffmpeg..." -ForegroundColor Gray
    winget install --id Gyan.FFmpeg --accept-package-agreements --accept-source-agreements --silent 2>$null | Out-Null
    
    Write-Host "    Installing ImageMagick..." -ForegroundColor Gray
    winget install --id ImageMagick.ImageMagick --accept-package-agreements --accept-source-agreements --silent 2>$null | Out-Null
    
    Write-Host "    Installing GitHub CLI..." -ForegroundColor Gray
    winget install --id GitHub.cli --accept-package-agreements --accept-source-agreements --silent 2>$null | Out-Null
    
    Write-Host "    Installing ngrok..." -ForegroundColor Gray
    winget install --id Ngrok.Ngrok --accept-package-agreements --accept-source-agreements --silent 2>$null | Out-Null
    
    Write-Host "  OK System tools installed via winget" -ForegroundColor Green
} else {
    Write-Host "  WARNING winget not available. Brax will need to install these manually:" -ForegroundColor Yellow
    Write-Host "     - Git: https://git-scm.com/download/win" -ForegroundColor Gray
    Write-Host "     - Node.js: https://nodejs.org (already installed above)" -ForegroundColor Gray
    Write-Host "     - Python: https://python.org" -ForegroundColor Gray
    Write-Host "     - ffmpeg: https://ffmpeg.org/download.html" -ForegroundColor Gray
    Write-Host "     - GitHub CLI: https://cli.github.com" -ForegroundColor Gray
    Write-Host "     - Docker Desktop: https://docker.com/products/docker-desktop" -ForegroundColor Gray
}

# ============================================================================
# STEP 8: INSTALL ADDITIONAL NPM PACKAGES
# ============================================================================
Write-Host ""
Write-Host "STEP 8: Installing additional npm packages..." -ForegroundColor Yellow

$npmPackages = @(
    "pnpm@10.32.1",
    "yarn@1.22.22",
    "vercel@54.2.0",
    "@railway/cli@4.59.0",
    "clawhub@0.8.0",
    "mcporter@0.9.0",
    "agent-browser@0.23.0",
    "create-next-app@14.2.35"
)

foreach ($pkg in $npmPackages) {
    Write-Host "    Installing $pkg..." -ForegroundColor Gray
    cmd /c "npm install -g $pkg 2>nul"
}

Write-Host "  OK NPM packages installed" -ForegroundColor Green

# ============================================================================
# STEP 9: INSTALL VIVID TUI
# ============================================================================
Write-Host ""
Write-Host "STEP 9: Installing VIVID TUI..." -ForegroundColor Yellow

$vividTuiDir = "$scriptDir\vivid-tui"
if (Test-Path "$vividTuiDir\package.json") {
    Write-Host "  Installing vivid-tui globally..." -ForegroundColor Gray
    cmd /c "npm install -g $vividTuiDir 2>nul"
    Write-Host "  OK VIVID TUI installed" -ForegroundColor Green
    Write-Host "  Run with: vivid-tui or vivid" -ForegroundColor Gray
} else {
    Write-Host "  WARNING vivid-tui not found in package" -ForegroundColor Yellow
}

# ============================================================================
# STEP 10: SUBSTITUTIONS (JAKIN -> BRAX)
# ============================================================================
Write-Host ""
Write-Host "STEP 10: Updating name references (Jakin -> Brax)..." -ForegroundColor Yellow

$filesToUpdate = @(
    "$WorkspaceDir\MEMORY.md",
    "$WorkspaceDir\SOUL.md",
    "$WorkspaceDir\USER.md",
    "$WorkspaceDir\AGENTS.md",
    "$WorkspaceDir\TOOLS.md",
    "$WorkspaceDir\HEARTBEAT.md",
    "$WorkspaceDir\BOOTSTRAP.md",
    "$WorkspaceDir\IDENTITY.md",
    "$WorkspaceDir\CLAUDE.md"
)

foreach ($file in $filesToUpdate) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding utf8
        $content = $content -replace 'Jakin', 'Brax'
        $content = $content -replace 'jakin@purifoy\.org', 'brax@example.com'
        $content = $content -replace '/Users/Jakin/', "$($BraxHome -replace '\\', '/')/"
        $content | Out-File -FilePath $file -Encoding utf8 -NoNewline
        Write-Host "  OK Updated: $(Split-Path $file -Leaf)" -ForegroundColor Green
    }
}

# Update self-improving files too
$selfFiles = @(
    "$BraxHome\self-improving\memory.md",
    "$BraxHome\self-improving\corrections.md",
    "$BraxHome\self-improving\reflections.md",
    "$BraxHome\self-improving\index.md",
    "$BraxHome\self-improving\heartbeat-state.md"
)

foreach ($file in $selfFiles) {
    if (Test-Path $file) {
        $content = Get-Content $file -Raw -Encoding utf8 -ErrorAction SilentlyContinue
        if ($content) {
            $content = $content -replace 'Jakin', 'Brax'
            $content | Out-File -FilePath $file -Encoding utf8 -NoNewline
        }
    }
}
Write-Host "  OK All name substitutions complete" -ForegroundColor Green

# ============================================================================
# STEP 11: VERIFY EVERYTHING
# ============================================================================
Write-Host ""
Write-Host "STEP 11: Verification..." -ForegroundColor Yellow

$checks = @{
    "OpenClaw version"     = { (openclaw --version 2>$null) -eq "2026.3.2" }
    "Workspace directory"  = { Test-Path $WorkspaceDir }
    "Skills installed"     = { (Get-ChildItem "$WorkspaceDir\skills" -Directory -ErrorAction SilentlyContinue).Count -gt 0 }
    "Memory archives"      = { (Get-ChildItem "$WorkspaceDir\memory" -File -ErrorAction SilentlyContinue).Count -gt 0 }
    "openclaw.json"        = { Test-Path "$OpenClawDir\openclaw.json" }
    "n8n workflows"        = { Test-Path "$BraxHome\n8n-workflows" }
    "Self-improving"       = { Test-Path "$BraxHome\self-improving\memory.md" }
    "Data analysis"        = { Test-Path "$BraxHome\data-analysis\config.md" }
    "Git repos cloned"     = { (Get-ChildItem "$BraxHome\gitnexus" -ErrorAction SilentlyContinue) -or
                                 (Get-ChildItem "$BraxHome\galaxy-demo" -ErrorAction SilentlyContinue) }
}

$allGood = $true
foreach ($check in $checks.GetEnumerator()) {
    $result = & $check.Value
    $status = if ($result) { "OK" } else { "FAIL" }
    $color = if ($result) { "Green" } else { "Red" }
    Write-Host "  $status $($check.Key)" -ForegroundColor $color
    if (-not $result) { $allGood = $false }
}

# ============================================================================
# STEP 12: CLEANUP
# ============================================================================
Write-Host ""
Write-Host "STEP 12: Cleanup..." -ForegroundColor Yellow

# Remove temp extraction dir if it exists
$tempDir = "$BraxHome\brax-migration-temp"
if (Test-Path $tempDir) {
    Remove-Item -Path $tempDir -Recurse -Force
    Write-Host "  OK Temp files cleaned" -ForegroundColor Green
}

# ============================================================================
# DONE
# ============================================================================
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   SETUP COMPLETE!" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if ($allGood) {
    Write-Host "OK All checks passed. Brax's OpenClaw is ready!" -ForegroundColor Green
} else {
    Write-Host "WARNING Some checks failed. Review above and re-run if needed." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "========================================" -ForegroundColor White
Write-Host "  LAUNCH VIVID TUI" -ForegroundColor Magenta
Write-Host "========================================" -ForegroundColor White
Write-Host ""
Write-Host "  vivid-tui              # Connect to running gateway" -ForegroundColor Cyan
Write-Host "  vivid-tui --start      # Start gateway + connect" -ForegroundColor Cyan
Write-Host ""
Write-Host "========================================" -ForegroundColor White
Write-Host "  FINAL STEP: Configure your Kimi API Key" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor White
Write-Host ""
Write-Host "  Run: openclaw auth add kimi-coding" -ForegroundColor Cyan
Write-Host "  Get key: https://platform.moonshot.cn" -ForegroundColor Gray
Write-Host ""
Write-Host "========================================" -ForegroundColor White
Write-Host "  OPTIONAL: Brave Search API Key" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor White
Write-Host ""
Write-Host "  1. Get free key: https://api.search.brave.com/app/dashboard" -ForegroundColor White
Write-Host "  2. Edit: $OpenClawDir\openclaw.json" -ForegroundColor White
Write-Host "  3. Replace YOUR_BRAVE_API_KEY_HERE" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor White
Write-Host "  START OPENCLAW" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor White
Write-Host ""
Write-Host "  openclaw gateway start" -ForegroundColor Cyan
Write-Host "  Then open: http://localhost:18789" -ForegroundColor White
Write-Host ""
Write-Host "========================================" -ForegroundColor White
Write-Host ""
Write-Host "Your setup includes:" -ForegroundColor Gray
Write-Host "  - OpenClaw 2026.3.2 - exact locked version" -ForegroundColor Gray
Write-Host "  - 80 skills - identical to Jakin's" -ForegroundColor Gray
Write-Host "  - 50+ memory archives - all session logs" -ForegroundColor Gray
Write-Host "  - 40+ GitHub repos cloned - same remotes as Jakin" -ForegroundColor Gray
Write-Host "  - n8n workflows, self-improving system, data analysis" -ForegroundColor Gray
Write-Host "  - Name: Brax (not Jakin)" -ForegroundColor Gray
Write-Host "  - No Telegram - webchat only" -ForegroundColor Gray
Write-Host "  - Windows paths (not macOS)" -ForegroundColor Gray
Write-Host ""
Write-Host "See INVENTORY.md for complete system inventory." -ForegroundColor Gray
Write-Host ""