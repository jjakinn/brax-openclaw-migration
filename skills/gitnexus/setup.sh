#!/bin/bash
# GitNexus Skill Setup Script
# Checks prerequisites and guides installation

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_NAME="GitNexus"

echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  GitNexus Skill - Setup & Verification${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo ""

# Check Node.js
echo -e "${BLUE}Checking Node.js...${NC}"
if command -v node > /dev/null 2>&1; then
    NODE_VERSION=$(node --version)
    echo -e "${GREEN}✓ Node.js found: $NODE_VERSION${NC}"
    
    # Check version (need >= 20)
    NODE_MAJOR=$(echo $NODE_VERSION | cut -d'v' -f2 | cut -d'.' -f1)
    if [ "$NODE_MAJOR" -ge 20 ]; then
        echo -e "${GREEN}✓ Node.js version OK (≥20)${NC}"
    else
        echo -e "${RED}✗ Node.js version too old. Need ≥20${NC}"
        echo "  Install from: https://nodejs.org/"
        exit 1
    fi
else
    echo -e "${RED}✗ Node.js not found${NC}"
    echo "  Install from: https://nodejs.org/"
    exit 1
fi

# Check npm
echo ""
echo -e "${BLUE}Checking npm...${NC}"
if command -v npm > /dev/null 2>&1; then
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✓ npm found: $NPM_VERSION${NC}"
else
    echo -e "${RED}✗ npm not found${NC}"
    exit 1
fi

# Check Python (for bridge)
echo ""
echo -e "${BLUE}Checking Python...${NC}"
if command -v python3 > /dev/null 2>&1; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ Python found: $PYTHON_VERSION${NC}"
else
    echo -e "${RED}✗ Python 3 not found${NC}"
    exit 1
fi

# Check for GitNexus
echo ""
echo -e "${BLUE}Checking GitNexus installation...${NC}"
GITNEXUS_FOUND=false

# Check various locations
check_gitnexus() {
    local path="$1"
    if [ -f "$path" ] && [ -x "$path" ]; then
        return 0
    fi
    return 1
}

# Try 'gitnexus' command
if command -v gitnexus > /dev/null 2>&1; then
    GITNEXUS_PATH=$(command -v gitnexus)
    GITNEXUS_VERSION=$(gitnexus --version 2>&1 || echo "unknown")
    echo -e "${GREEN}✓ GitNexus found in PATH${NC}"
    echo -e "  Location: $GITNEXUS_PATH"
    echo -e "  Version: $GITNEXUS_VERSION"
    GITNEXUS_FOUND=true
    
# Check common locations
elif check_gitnexus "$HOME/gitnexus/gitnexus/dist/cli/index.js"; then
    echo -e "${YELLOW}! GitNexus found in local clone${NC}"
    echo -e "  Location: $HOME/gitnexus/gitnexus/dist/cli/index.js"
    echo -e "  Add to PATH or set GITNEXUS_PATH environment variable"
    
elif check_gitnexus "$HOME/.npm-global/bin/gitnexus"; then
    echo -e "${YELLOW}! GitNexus found in npm-global${NC}"
    echo -e "  Location: $HOME/.npm-global/bin/gitnexus"
    echo -e "  Add to PATH: export PATH=\"$HOME/.npm-global/bin:\$PATH\""
    
else
    echo -e "${RED}✗ GitNexus not found${NC}"
fi

# Installation options
echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"

if [ "$GITNEXUS_FOUND" = true ]; then
    echo -e "${GREEN}GitNexus skill is ready to use!${NC}"
    echo ""
    echo "Quick test:"
    echo "  python3 $SCRIPT_DIR/gitnexus_bridge.py version"
    echo ""
    echo "Available tools:"
    echo "  gitnexus_analyze     - Index a repository"
    echo "  gitnexus_query       - Search the knowledge graph"
    echo "  gitnexus_context     - Get symbol context"
    echo "  gitnexus_impact      - Blast radius analysis"
    echo "  gitnexus_list        - List indexed repos"
    echo "  gitnexus_status      - Check index status"
    echo ""
else
    echo -e "${YELLOW}GitNexus needs to be installed${NC}"
    echo ""
    echo "Installation options:"
    echo ""
    echo "Option 1: Global install (recommended)"
    echo -e "  ${BLUE}npm install -g gitnexus${NC}"
    echo ""
    echo "Option 2: Local clone + build"
    echo -e "  ${BLUE}git clone https://github.com/abhigyanpatwari/GitNexus.git ~/gitnexus${NC}"
    echo -e "  ${BLUE}cd ~/gitnexus/gitnexus-shared && npm install && npm run build${NC}"
    echo -e "  ${BLUE}cd ~/gitnexus/gitnexus && npm install && npm run build${NC}"
    echo -e "  ${BLUE}export GITNEXUS_PATH=~/gitnexus/gitnexus/dist/cli/index.js${NC}"
    echo ""
    echo "Option 3: Use web UI (no install)"
    echo -e "  Visit: ${BLUE}https://gitnexus.vercel.app${NC}"
    echo "  Upload code as ZIP for analysis"
    echo ""
    echo -e "${YELLOW}Note:${NC} Option 1 requires native dependencies that may fail on"
    echo "some systems. If it fails, try Option 2 or use the web UI."
fi

echo ""
echo -e "${BLUE}═══════════════════════════════════════════════════${NC}"
echo "Skill location: $SCRIPT_DIR"
echo "Documentation: $SCRIPT_DIR/SKILL.md"
echo ""
