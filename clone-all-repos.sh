#!/bin/bash
# Clone All GitHub Repos — Brax Setup
# Based on Jakin's exact repo collection

set -e

echo "🗂️  Cloning all GitHub repositories..."
echo "======================================"
echo ""

BASE_DIR="$HOME"
cd "$BASE_DIR"

# Function to clone or skip if exists
clone_repo() {
    local url="$1"
    local dest="$2"
    
    if [ -d "$dest/.git" ]; then
        echo "  ✅ Already exists: $dest"
        return
    fi
    
    if [ -d "$dest" ]; then
        echo "  ⚠️  Directory exists but no .git: $dest (skipping)"
        return
    fi
    
    echo "  📥 Cloning: $url → $dest"
    git clone "$url" "$dest" || echo "  ❌ Failed: $url"
}

# Core / AI Infrastructure
clone_repo "https://github.com/abhigyanpatwari/GitNexus.git" "gitnexus"
clone_repo "https://github.com/abhigyanpatwari/GitNexus.git" "gitnexus-tool"
clone_repo "https://github.com/jjakinn/Hermes-4-Brax.git" "hermes-for-brax"
clone_repo "https://github.com/NousResearch/hermes-agent.git" ".hermes/hermes-agent"
clone_repo "https://github.com/Coding-Solo/godot-mcp.git" "godot-mcp"

# Club Penguin / Game Development
clone_repo "https://github.com/project-flipper/ClubPenguin.git" "ClubPenguin"
clone_repo "https://github.com/clubpenguinadvanced/cpadvanced-client.git" "cpadvanced-client"
clone_repo "https://github.com/abarichello/cp-swf.git" "cp-swf"
clone_repo "https://github.com/Ep8Script/Club_Penguin_Minigames.git" "cp-minigames"
clone_repo "https://github.com/solero/houdini.git" "cpps-houdini"
clone_repo "https://github.com/wizguin/mammoth.git" "cpps-mammoth"
clone_repo "https://github.com/nhaar/Waddle-Forever.git" "waddle-forever"
clone_repo "https://github.com/wizguin/yukon.git" "yukon-client"
clone_repo "https://github.com/wizguin/yukon-server.git" "yukon-server"
clone_repo "https://github.com/clubpenguinadvanced/project-aether.git" "project-aether"
clone_repo "https://github.com/aprilx246/ClubPenguin.git" "ClawMind/clubpenguin-repo"
clone_repo "https://github.com/project-flipper/ClubPenguin.git" "ClawMind/flipper-client"
clone_repo "https://github.com/project-flipper/Island.git" "ClawMind/flipper-island"
clone_repo "https://github.com/liberatedpixelcup/Universal-LPC-Spritesheet-Character-Generator.git" "ClawMind/lpc-generator"

# AI / ML / Generative Models
clone_repo "https://github.com/comfyanonymous/ComfyUI.git" "ComfyUI"
clone_repo "https://github.com/TencentCloud/CubeSandbox.git" "ClawMind/CubeSandbox"
clone_repo "https://github.com/PurpleAILAB/Decepticon.git" "ClawMind/Decepticon"
clone_repo "https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1.git" "ClawMind/Hunyuan3D-2.1"
clone_repo "https://github.com/Tencent-Hunyuan/HunyuanImage-3.0.git" "ClawMind/HunyuanImage-3.0"
clone_repo "https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5.git" "ClawMind/HunyuanVideo-1.5"
clone_repo "https://github.com/HQarroum/docker-android.git" "ClawMind/docker-android"
clone_repo "https://github.com/facebookresearch/ai4animationpy.git" "ai4animationpy"
clone_repo "https://github.com/nv-tlabs/lyra.git" "lyra"

# SaaS / API Projects
clone_repo "https://github.com/Glztch/ssl-analyzer-api.git" "api-projects/ssl-analyzer"
clone_repo "https://github.com/jjakinn/breach-checker-api.git" "api-projects/breach-checker"
clone_repo "https://github.com/jjakinn/ip-reputation-api.git" "api-projects/ip-reputation"
clone_repo "https://github.com/jjakinn/leadvault-automation.git" "leadvault-automation"
clone_repo "https://github.com/jjakinn/leadvault-site.git" "leadvault-site"
clone_repo "https://github.com/jjakinn/rize-clone.git" "rize-clone"
clone_repo "https://github.com/eonsystemspbc/fly-brain.git" "fly-brain"
clone_repo "https://github.com/dunamismax/terminalphone.git" "terminalphone"
clone_repo "https://github.com/uberchel/TitanEngine.git" "TitanEngine"

# Other / Utility
clone_repo "https://github.com/pyenv/pyenv.git" ".pyenv"
clone_repo "https://github.com/4R7I5T/CL1_LLM_Encoder.git" "CL1_LLM_Encoder"
clone_repo "https://github.com/Adam-CAD/CADAM.git" "CADAM"
clone_repo "https://github.com/NawfalMotii79/PLFM_RADAR.git" "PLFM_RADAR"
clone_repo "https://github.com/PolymathicAI/the_well.git" "the_well"
clone_repo "https://github.com/dimensionalOS/dimos.git" "dimos"
clone_repo "https://github.com/asimovinc/asimov-v0.git" "asimov-v0"
clone_repo "https://github.com/lightningpixel/modly.git" "modly"
clone_repo "https://github.com/elder-plinius/OBLITERATUS.git" "OBLITERATUS"
clone_repo "https://github.com/iamlukethedev/Claw3D.git" "Claw3D"
clone_repo "https://github.com/fathyb/carbonyl.git" "carbonyl"
clone_repo "https://github.com/dmtrKovalenko/fff.nvim.git" "fff.nvim"
clone_repo "https://github.com/siddharthvaddem/openscreen.git" "openscreen"
clone_repo "https://github.com/ultraworkers/claw-code.git" "claw-code"
clone_repo "https://github.com/tomasferrerasdev/try-html-in-canvas.git" "try-html-in-canvas"
clone_repo "https://github.com/pascalorg/editor.git" "editor"
clone_repo "https://github.com/ruzin/stenoai.git" "stenoai"
clone_repo "https://github.com/ruvnet/RuView.git" "RuView"
clone_repo "https://github.com/bddicken/tuitter.git" "tuitter"

# Private repos (Brax must fork or get access)
echo ""
echo "⚠️  Private repos (requires Brax's own GitHub access):"
echo "   - https://github.com/jjakinn/ssl-analyzer-api (or use Glztch fork)"
echo "   - https://github.com/jjakinn/breach-checker-api"
echo "   - https://github.com/jjakinn/ip-reputation-api"
echo "   - https://github.com/jjakinn/leadvault-automation"
echo "   - https://github.com/jjakinn/leadvault-site"
echo "   - https://github.com/jjakinn/rize-clone"
echo "   - https://github.com/jjakinn/Hermes-4-Brax (fork this for your own)"
echo ""

echo "✅ Repo cloning complete!"
echo ""
echo "Next: Run ./install-tools.sh to install all software."
