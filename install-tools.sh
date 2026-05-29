#!/bin/bash
# Install All Tools — Brax Setup
# Based on Jakin's exact tool collection

set -e

echo "🛠️  Installing all tools..."
echo "==========================="
echo ""

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "📦 Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    eval "$(/opt/homebrew/bin/brew shellenv)"
fi

echo "✅ Homebrew ready"
echo ""

# Core Development
echo "🔧 Core Development Tools..."
brew install gh git node@22 python@3.14 pyenv deno docker docker-completion docker-compose colima lima redis mysql postgresql@16 sqlite gcc

# Media / Graphics
echo "🎨 Media & Graphics..."
brew install ffmpeg imagemagick vips webp sdl2 giflib libpng libtiff libheif openjpeg libraw aom x264 x265 svt-av1 opus lame

# Security / Networking
echo "🔒 Security & Networking..."
brew install cloudflared gnupg openssl@3 httrack yt-dlp

# Utilities
echo "🛠️  Utilities..."
brew install ripgrep htop tree-sitter pkgconf autoconf m4 readline ncurses gettext pcre2 xz lz4 zstd zlib-ng-compat

# AI / ML
echo "🤖 AI & ML..."
brew install ollama mlx mlx-c hdf5

# Additional formulas
echo "📚 Additional packages..."
brew install abseil aom brotli c-ares ca-certificates cairo certifi cfitsio cgif dav1d expat fftw fontconfig freetype fribidi gdk-pixbuf gmp gnutls gpgme gpgmepp graphite2 harfbuzz highway icu4c@78 imath isl jpeg-turbo jpeg-xl krb5 lame libaec libarchive libassuan libb2 libdatrie libde265 libdeflate libdicom libevent libexif libgcrypt libgpg-error libidn2 libimagequant libksba libmatio libmpc libnghttp2 libnghttp3 libngtcp2 libomp librsvg libtasn1 libthai libtool libultrahdr libunistring libusb libuv libvmaf libvpx libx11 libxau libxcb libxdmcp libxext libxml2 libxrender little-cms2 lzip lzo m4 mpdecimal mpfr mozjpeg nettle npth nspr nss openexr openjph openslide p11-kit pango pinentry pixman poppler protobuf python@3.14 shared-mime-info simdjson simdutf svt-av1 unbound uthash uvwasi xorgproto

# Casks
echo "📱 Installing casks..."
brew install --cask anki dotnet-runtime miniconda ngrok telegram

echo ""
echo "✅ Homebrew packages installed!"
echo ""

# Node.js tools
echo "📦 Installing global npm packages..."
npm install -g pnpm@10.32.1
npm install -g yarn@1.22.22
npm install -g @microsoft/power-apps-cli@0.9.1
npm install -g @microsoft/power-apps@1.0.17
npm install -g @railway/cli@4.59.0
npm install -g agent-browser@0.23.0
npm install -g clawhub@0.8.0
npm install -g create-next-app@14.2.35
npm install -g mcporter@0.9.0
npm install -g n8n@2.15.0
npm install -g openclaw@2026.3.2
npm install -g vercel@54.2.0

echo ""
echo "✅ NPM packages installed!"
echo ""

# Python tools
echo "🐍 Installing Python tools..."
curl -LsSf https://astral.sh/uv/install.sh | sh
pip3 install --upgrade pip

echo ""
echo "✅ Python tools installed!"
echo ""

# Rust
echo "🦀 Installing Rust..."
if ! command -v rustup &> /dev/null; then
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    source "$HOME/.cargo/env"
fi

echo ""
echo "✅ Rust installed!"
echo ""

# Ollama models
echo "🧠 Pulling Ollama models..."
ollama pull llama3.2:3b
ollama pull dolphin-uncensored:latest
ollama pull dolphin3:8b
ollama pull qwen2.5-coder:7b
ollama pull qwen2.5:7b
ollama pull nous-hermes2:latest
ollama pull dolphin-llama3:8b
ollama pull llama3.2:latest
ollama pull glm-4.7-flash:latest

echo ""
echo "✅ Ollama models pulled!"
echo ""

# Git configuration
echo "⚙️  Configuring git..."
git config --global user.email "brax@example.com"
git config --global user.name "Brax"
git config --global credential.helper store

echo ""
echo "==========================="
echo "🎉 All tools installed!"
echo "==========================="
echo ""
echo "Next steps:"
echo "1. Configure API keys (Kimi, Brave, GitHub, etc.)"
echo "2. Run ./setup.sh for OpenClaw workspace setup"
echo "3. Copy .zshrc.brax to ~/.zshrc"
echo ""
