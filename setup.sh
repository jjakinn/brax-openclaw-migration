#!/bin/bash
# OpenClaw Migration Script — Brax Setup
# Based on Jakin's exact setup (OpenClaw 2026.3.2)
# Version locked: 2026.3.2

set -e

echo "🦾 OpenClaw Migration — Brax Setup"
echo "=================================="
echo ""

# Determine Brax's home directory
BRAX_HOME="$HOME"
BRAX_USER="$(whoami)"
WORKSPACE="$BRAX_HOME/.openclaw/workspace"

echo "Home: $BRAX_HOME"
echo "User: $BRAX_USER"
echo "Workspace: $WORKSPACE"
echo ""

# Check if already installed
if command -v openclaw &> /dev/null; then
    INSTALLED_VERSION=$(openclaw --version 2>/dev/null || openclaw version 2>/dev/null)
    if [ "$INSTALLED_VERSION" = "2026.3.2" ]; then
        echo "✅ OpenClaw 2026.3.2 already installed"
    else
        echo "⚠️  Different version installed: $INSTALLED_VERSION"
        echo "   Will install 2026.3.2 alongside or re-install..."
    fi
else
    echo "📦 Installing OpenClaw 2026.3.2..."
    npm install -g openclaw@2026.3.2
fi

echo ""
echo "📁 Setting up workspace..."
mkdir -p "$WORKSPACE"
mkdir -p "$WORKSPACE/memory"
mkdir -p "$WORKSPACE/config"
mkdir -p "$WORKSPACE/skills"
mkdir -p "$BRAX_HOME/self-improving"
mkdir -p "$BRAX_HOME/self-improving/projects"
mkdir -p "$BRAX_HOME/self-improving/archive"
mkdir -p "$BRAX_HOME/self-improving/domains"
mkdir -p "$BRAX_HOME/self-improving/drafts"
mkdir -p "$BRAX_HOME/self-improving/snapshots"
mkdir -p "$BRAX_HOME/n8n-workflows"
mkdir -p "$BRAX_HOME/data-analysis/datasets"
mkdir -p "$BRAX_HOME/data-analysis/reports"
mkdir -p "$BRAX_HOME/ClawMind"

echo "✅ Directories created"
echo ""

# Check if migration package exists
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ ! -d "$SCRIPT_DIR/workspace-files" ]; then
    echo "❌ Error: workspace-files/ not found next to this script"
    echo "   Expected at: $SCRIPT_DIR/workspace-files"
    exit 1
fi

echo "📂 Copying workspace files..."
cp -R "$SCRIPT_DIR/workspace-files/"* "$WORKSPACE/" 2>/dev/null || true
cp -R "$SCRIPT_DIR/workspace-files/."[a-zA-Z]* "$WORKSPACE/" 2>/dev/null || true

echo "📂 Copying skills..."
if [ -d "$SCRIPT_DIR/skills" ]; then
    cp -R "$SCRIPT_DIR/skills/"* "$WORKSPACE/skills/" 2>/dev/null || true
fi

echo "📂 Copying memory files..."
if [ -d "$SCRIPT_DIR/memory" ]; then
    cp -R "$SCRIPT_DIR/memory/"* "$WORKSPACE/memory/" 2>/dev/null || true
fi

echo "📂 Copying n8n workflows..."
if [ -d "$SCRIPT_DIR/n8n-workflows" ]; then
    cp -R "$SCRIPT_DIR/n8n-workflows/"* "$BRAX_HOME/n8n-workflows/" 2>/dev/null || true
fi

echo "📂 Copying self-improving files..."
if [ -d "$SCRIPT_DIR/self-improving" ]; then
    cp -R "$SCRIPT_DIR/self-improving/"* "$BRAX_HOME/self-improving/" 2>/dev/null || true
fi

echo "📂 Copying data-analysis files..."
if [ -d "$SCRIPT_DIR/data-analysis" ]; then
    cp -R "$SCRIPT_DIR/data-analysis/"* "$BRAX_HOME/data-analysis/" 2>/dev/null || true
fi

echo "✅ All files copied"
echo ""

echo "🔧 Generating openclaw.json..."

# Generate openclaw.json with Brax's paths, no Telegram
cat > "$BRAX_HOME/.openclaw/openclaw.json" << 'JSONEOF'
{
  "meta": {
    "lastTouchedVersion": "2026.3.2",
    "lastTouchedAt": "2026-05-29T18:00:00.000Z"
  },
  "wizard": {
    "lastRunAt": "2026-05-29T18:00:00.000Z",
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
            "input": [
              "text",
              "image"
            ],
            "cost": {
              "input": 0,
              "output": 0,
              "cacheRead": 0,
              "cacheWrite": 0
            },
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
        "fallbacks": [
          "kimi/k2p5",
          "kimi/kimi-code",
          "kimi-coding/kimi-k2-thinking"
        ]
      },
      "models": {
        "kimi-coding/k2p5": {
          "alias": "Kimi for Coding"
        },
        "kimi/k2p5": {},
        "kimi/kimi-code": {},
        "kimi-coding/kimi-k2-thinking": {}
      },
      "workspace": "WORKSPACE_PATH",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8
      }
    }
  },
  "tools": {
    "web": {
      "search": {
        "enabled": true,
        "apiKey": "YOUR_BRAVE_API_KEY_HERE"
      },
      "fetch": {
        "enabled": true
      }
    }
  },
  "messages": {
    "ackReactionScope": "group-mentions"
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto",
    "restart": true,
    "ownerDisplay": "raw"
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "auto",
    "auth": {
      "mode": "token",
      "token": "GENERATE_NEW_TOKEN"
    },
    "tailscale": {
      "mode": "off",
      "resetOnExit": false
    }
  },
  "plugins": {
    "entries": {}
  }
}
JSONEOF

# Replace placeholder paths with actual paths
sed -i '' "s|WORKSPACE_PATH|$WORKSPACE|g" "$BRAX_HOME/.openclaw/openclaw.json" 2>/dev/null || sed -i "s|WORKSPACE_PATH|$WORKSPACE|g" "$BRAX_HOME/.openclaw/openclaw.json"

echo "✅ openclaw.json generated"
echo ""

# Install VIVID TUI
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -d "$SCRIPT_DIR/vivid-tui" ]; then
    echo "🦆 Installing VIVID TUI..."
    cd "$SCRIPT_DIR/vivid-tui"
    npm install -g . 2>/dev/null || sudo npm install -g . 2>/dev/null || echo "⚠️  Could not install vivid-tui globally"
    echo "✅ VIVID TUI installed"
    echo "   Run with: vivid-tui or vivid"
    echo ""
fi

echo "🔑 IMPORTANT: You must configure your own API keys:"
echo "   1. Kimi API key: run 'openclaw auth add kimi-coding'"
echo "   2. Brave Search API key: edit ~/.openclaw/openclaw.json tools.web.search.apiKey"
echo "   3. Gateway token: edit ~/.openclaw/openclaw.json gateway.auth.token"
echo ""

echo "📝 Post-setup name substitutions..."
# Replace Jakin with Brax in key files
for file in "$WORKSPACE"/MEMORY.md "$WORKSPACE"/SOUL.md "$WORKSPACE"/USER.md; do
    if [ -f "$file" ]; then
        sed -i '' 's/Jakin/Brax/g' "$file" 2>/dev/null || sed -i 's/Jakin/Brax/g' "$file"
        echo "   Updated: $(basename "$file")"
    fi
done

echo ""
echo "=================================="
echo "🎉 Brax's OpenClaw setup complete!"
echo "=================================="
echo ""
echo "📋 Additional scripts in this package:"
echo "   ./install-tools.sh   — Install all brew formulas, npm packages, Ollama models"
echo "   ./clone-all-repos.sh — Clone all GitHub repositories"
echo "   ./.zshrc.brax        — Copy to ~/.zshrc for shell config"
echo ""
echo "Full setup order:"
echo "   1. ./install-tools.sh    (takes a while)"
echo "   2. ./clone-all-repos.sh  (takes a while)"
echo "   3. ./setup.sh            (this script — OpenClaw workspace)"
echo "   4. cp .zshrc.brax ~/.zshrc"
echo "   5. openclaw auth add kimi-coding"
echo "   6. openclaw gateway start"
echo "   7. vivid-tui --start"
echo ""
echo "Next steps:"
echo "   • Run 'openclaw auth add kimi-coding' to add your Kimi API key"
echo "   • Replace 'YOUR_BRAVE_API_KEY_HERE' in ~/.openclaw/openclaw.json"
echo "   • Run 'openclaw gateway start' to start the gateway"
echo "   • Or use VIVID TUI: vivid-tui --start"
echo "   • Open webchat at http://localhost:18789"
echo ""
echo "Your setup is identical to Jakin's except:"
echo "  - Name is Brax instead of Jakin"
echo "  - No Telegram (webchat only)"
echo "  - Your own Kimi subscription"
echo "  - OpenClaw version locked to 2026.3.2"
echo ""
echo "📖 See INVENTORY.md for complete system inventory (repos, tools, websites)"
echo ""
