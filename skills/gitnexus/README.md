# GitNexus Skill for OpenClaw

**Code intelligence engine for AI agents.** Index any codebase into a knowledge graph and query it with 10+ specialized tools.

## 🚀 Quick Start

```bash
# 1. Check prerequisites
./setup.sh

# 2. Install GitNexus (choose one)
npm install -g gitnexus              # Global install
git clone https://github.com/abhigyanpatwari/GitNexus.git ~/gitnexus  # Local build

# 3. Start using
python3 gitnexus_bridge.py analyze path="~/my-project"
```

## 📁 Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Full documentation with all tools and parameters |
| `EXAMPLES.md` | Real-world usage examples and workflows |
| `gitnexus_bridge.py` | Python bridge to GitNexus CLI |
| `gitnexus-tool` | Bash wrapper for OpenClaw integration |
| `tools.json` | Tool definitions for OpenClaw |
| `setup.sh` | Prerequisites checker and setup guide |

## 🛠️ Available Tools

### Core Tools
- `gitnexus_analyze` — Index repository into knowledge graph
- `gitnexus_query` — Hybrid search (BM25 + semantic)
- `gitnexus_context` — 360° symbol view
- `gitnexus_impact` — Blast radius analysis
- `gitnexus_detect_changes` — Git-diff impact
- `gitnexus_cypher` — Raw graph queries

### Utility Tools
- `gitnexus_list` — List indexed repos
- `gitnexus_status` — Check index status
- `gitnexus_wiki` — Generate documentation
- `gitnexus_rename` — Multi-file coordinated rename
- `gitnexus_clean` — Delete indexes
- `gitnexus_serve` — HTTP server for web UI

## 🎯 Common Workflows

### Explore Unfamiliar Code
```xml
<gitnexus_analyze path="~/new-project" />
<gitnexus_query query="authentication flow" />
<gitnexus_context name="AuthService" />
```

### Safe Refactoring
```xml
<gitnexus_impact target="oldFunction" direction="upstream" />
<gitnexus_rename symbol_name="oldFunction" new_name="newFunction" dry_run="true" />
```

### Pre-commit Check
```xml
<gitnexus_detect_changes scope="staged" />
<gitnexus_impact target="changedSymbol" direction="upstream" />
```

## 📊 Supported Languages

TypeScript, JavaScript, Python, Java, Kotlin, C#, Go, Rust, PHP, Ruby, Swift, C, C++, Dart

## 🔗 Integration with ClawMind

GitNexus provides **structural intelligence** (call graphs, dependencies). ClawMind provides **semantic intelligence** (meaning, decisions, history). Together = complete codebase awareness.

## 📚 Documentation

- Full docs: `SKILL.md`
- Examples: `EXAMPLES.md`
- GitNexus repo: https://github.com/abhigyanpatwari/GitNexus
- Web UI: https://gitnexus.vercel.app

## ⚠️ Requirements

- Node.js ≥ 20
- Python 3
- GitNexus CLI (install via npm or build from source)

## 🐛 Troubleshooting

**"GitNexus not found"**
```bash
npm install -g gitnexus
# or set environment variable:
export GITNEXUS_PATH=/path/to/gitnexus
```

**Native build failures**
- Use web UI: https://gitnexus.vercel.app
- Or try local build with `npm install --omit=optional`

**Index out of date**
```xml
<gitnexus_analyze force="true" />
```

## 📄 License

- Skill: MIT
- GitNexus: PolyForm-Noncommercial-1.0.0
