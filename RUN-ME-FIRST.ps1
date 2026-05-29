# RUN-ME-FIRST.ps1
# Brax OpenClaw Setup - One-Click Entry Point
# This is the ONLY file you need to run. It does everything else.

# Ensure we can run scripts
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$setupScript = Join-Path $scriptDir "setup-windows.ps1"

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   Brax OpenClaw Setup - One-Click" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

if (-not (Test-Path $setupScript)) {
    Write-Host "ERROR: setup-windows.ps1 not found in the same folder!" -ForegroundColor Red
    Write-Host "Make sure you extracted the entire brax-openclaw-migration.zip and didn't move files." -ForegroundColor Red
    Write-Host ""
    Write-Host "Expected at: $setupScript" -ForegroundColor Gray
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Found setup script: $setupScript" -ForegroundColor Green
Write-Host "Starting full setup..." -ForegroundColor Yellow
Write-Host ""

# Run the full setup
& $setupScript

# Pause at the end so Brax can read the output
Write-Host ""
Read-Host "Press Enter to close this window"
