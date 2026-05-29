# GitNexus Skill

**GitNexus integration for OpenClaw** — Zero-server code intelligence engine. Index any codebase into a knowledge graph and query it via CLI or HTTP API.

## Overview

GitNexus is a client-side knowledge graph creator that parses codebases using Tree-sitter ASTs, builds a graph of symbols/dependencies/call chains, and exposes it through smart tools so AI agents never miss code context.

This skill provides:
- **Automatic indexing** — Run `gitnexus analyze` on any repo
- **Hybrid search** — BM25 + semantic + RRF for finding relevant code
- **Impact analysis** — Blast radius before making changes
- **360° context** — Full symbol view with incoming/outgoing refs
- **Multi-repo support** — Analyze across repository boundaries

## Prerequisites

### Option 1: Global Install (Recommended)
```bash
npm install -g gitnexus
```

### Option 2: Local Clone
```bash
git clone https://github.com/abhigyanpatwari/GitNexus.git ~/gitnexus
cd ~/gitnexus/gitnexus-shared && npm install && npm run build
cd ~/gitnexus/gitnexus && npm install && npm run build
```

### Verify Installation
```bash
gitnexus --version
```

## Tools

### `gitnexus_analyze`
Index a repository into the knowledge graph.

**Usage:**
```xml
<gitnexus_analyze path="./my-project" force="false" embeddings="true" skills="true" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `path` | string | `.` | Path to repository |
| `force` | boolean | `false` | Force full re-index |
| `embeddings` | boolean | `true` | Generate embeddings (slower, better search) |
| `skills` | boolean | `false` | Generate repo-specific skill files |
| `skip_agents_md` | boolean | `false` | Preserve custom AGENTS.md edits |

**Example:**
```xml
<gitnexus_analyze path="~/projects/world-monitor" embeddings="true" />
```

---

### `gitnexus_query`
Hybrid search across the knowledge graph.

**Usage:**
```xml
<gitnexus_query repo="my-project" query="authentication middleware" limit="10" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name (optional if only one indexed) |
| `query` | string | required | Search query |
| `limit` | number | `10` | Max results |

**Returns:**
- Definitions (functions, classes, interfaces)
- Process flows
- Clustered communities
- Relevance scores

**Example:**
```xml
<gitnexus_query query="how does user login work" />
```

---

### `gitnexus_context`
360-degree symbol view with full context.

**Usage:**
```xml
<gitnexus_context repo="my-project" name="validateUser" type="function" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `name` | string | required | Symbol name |
| `type` | string | auto | Symbol type (function, class, etc.) |

**Returns:**
- Symbol metadata (file, line, kind)
- Incoming refs (what calls this)
- Outgoing refs (what this calls)
- Process participation
- Cluster membership

**Example:**
```xml
<gitnexus_context name="VideoPanel" type="class" />
```

---

### `gitnexus_impact`
Blast radius analysis for changes.

**Usage:**
```xml
<gitnexus_impact repo="my-project" target="UserService" direction="upstream" depth="2" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `target` | string | required | Symbol to analyze |
| `direction` | string | `upstream` | `upstream` (depends on) or `downstream` (depends from) |
| `depth` | number | `2` | Analysis depth |
| `min_confidence` | number | `0.8` | Minimum relationship confidence |

**Returns:**
- Direct dependents (will break)
- Indirect dependents (likely affected)
- Confidence scores per relationship
- Risk level assessment

**Example:**
```xml
<gitnexus_impact target="authMiddleware" direction="upstream" depth="3" />
```

---

### `gitnexus_detect_changes`
Git-diff impact analysis.

**Usage:**
```xml
<gitnexus_detect_changes repo="my-project" scope="staged" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `scope` | string | `all` | `all`, `staged`, or `unstaged` |

**Returns:**
- Changed symbols count
- Affected processes
- Risk level (low/medium/high)
- Files and symbols impacted

---

### `gitnexus_cypher`
Raw Cypher graph queries.

**Usage:**
```xml
<gitnexus_cypher repo="my-project" query="MATCH (f:Function) WHERE f.name CONTAINS 'auth' RETURN f" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `query` | string | required | Cypher query |

**Example:**
```xml
<gitnexus_cypher query="MATCH (c:Community)<-[:MEMBER_OF]-(fn) WHERE c.heuristicLabel = 'Authentication' RETURN fn.name" />
```

---

### `gitnexus_rename`
Multi-file coordinated rename with impact analysis.

**Usage:**
```xml
<gitnexus_rename repo="my-project" symbol_name="oldName" new_name="newName" dry_run="true" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `symbol_name` | string | required | Current symbol name |
| `new_name` | string | required | New symbol name |
| `dry_run` | boolean | `true` | Preview changes without applying |

---

### `gitnexus_list`
List all indexed repositories.

**Usage:**
```xml
<gitnexus_list />
```

---

### `gitnexus_status`
Check index status for current/specified repo.

**Usage:**
```xml
<gitnexus_status repo="my-project" />
```

---

### `gitnexus_wiki`
Generate repository wiki from knowledge graph.

**Usage:**
```xml
<gitnexus_wiki repo="my-project" model="gpt-4o-mini" />
```

**Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| `repo` | string | auto | Repository name |
| `model` | string | `gpt-4o-mini` | LLM model for generation |
| `base_url` | string | - | Custom API base URL |

---

### `gitnexus_serve`
Start local HTTP server for web UI bridge.

**Usage:**
```xml
<gitnexus_serve port="3001" />
```

**Parameters:**
| Param | Type | Default | Description |
| `port` | number | `3001` | HTTP server port |

**Notes:**
- Runs in background
- Web UI auto-detects at `gitnexus.vercel.app`
- Provides HTTP API for all indexed repos

---

## Supported Languages

| Language | Imports | Bindings | Exports | Heritage | Type Annotations | Constructor Inference | Config | Frameworks | Entry Points |
|----------|---------|----------|---------|----------|------------------|----------------------|--------|------------|--------------|
| TypeScript | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| JavaScript | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| Python | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Java | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| Kotlin | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| C# | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Go | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Rust | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| PHP | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Ruby | ✓ | — | ✓ | ✓ | — | ✓ | — | ✓ | ✓ |
| Swift | — | — | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| C | — | — | ✓ | — | ✓ | ✓ | — | ✓ | ✓ |
| C++ | — | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |
| Dart | ✓ | — | ✓ | ✓ | ✓ | ✓ | — | ✓ | ✓ |

## Workflow Examples

### Explore Unfamiliar Codebase
```xml
<gitnexus_analyze path="~/new-project" embeddings="true" />
<gitnexus_query query="authentication flow" />
<gitnexus_context name="AuthService" />
<gitnexus_impact target="AuthService" direction="upstream" />
```

### Safe Refactoring
```xml
<gitnexus_impact target="oldFunctionName" direction="upstream" depth="3" />
<gitnexus_rename symbol_name="oldFunctionName" new_name="newFunctionName" dry_run="true" />
<!-- Review changes, then: -->
<gitnexus_rename symbol_name="oldFunctionName" new_name="newFunctionName" dry_run="false" />
```

### Pre-commit Validation
```xml
<gitnexus_detect_changes scope="staged" />
<gitnexus_impact target="changedSymbol" direction="upstream" />
```

### Multi-repo Analysis
```xml
<gitnexus_group_create name="backend-services" />
<gitnexus_group_add name="backend-services" repo="api-gateway" />
<gitnexus_group_add name="backend-services" repo="auth-service" />
<gitnexus_group_sync name="backend-services" />
<gitnexus_group_query name="backend-services" query="login flow" />
```

## Architecture

```
┌─────────────────┐     ┌─────────────┐     ┌─────────────────┐
│  OpenClaw Agent │────▶│ GitNexus    │────▶│  Knowledge      │
│  (This Skill)   │     │  MCP/CLI    │     │  Graph DB       │
└─────────────────┘     └─────────────┘     └─────────────────┘
                              │
                              ▼
                       ┌─────────────┐
                       │ Tree-sitter │
                       │   Parser    │
                       └─────────────┘
```

**Storage:**
- Index stored in `.gitnexus/` (gitignored) within each repo
- Global registry at `~/.gitnexus/registry.json`

## Configuration

### Environment Variables
| Var | Description |
|-----|-------------|
| `GITNEXUS_PATH` | Custom path to gitnexus binary |
| `GITNEXUS_API_URL` | HTTP API base URL (default: http://localhost:3001) |
| `OPENAI_API_KEY` | For wiki generation |

### Per-Project Config
Create `.gitnexus/config.json` in repo root:
```json
{
  "excludePatterns": ["*.test.ts", "**/node_modules/**"],
  "entryPoints": ["src/index.ts", "src/server.ts"],
  "framework": "express"
}
```

## Troubleshooting

### "gitnexus command not found"
```bash
npm install -g gitnexus
# or
export GITNEXUS_PATH=/path/to/gitnexus/dist/cli/index.js
```

### Index Out of Date
```xml
<gitnexus_analyze force="true" />
```

### Large Repositories
```xml
<gitnexus_analyze skip_embeddings="true" />
```

### Native Dependencies Fail
Use web version at `gitnexus.vercel.app` or HTTP bridge:
```xml
<gitnexus_serve port="3001" />
```

## Resources

- **GitHub:** https://github.com/abhigyanpatwari/GitNexus
- **Web UI:** https://gitnexus.vercel.app
- **Documentation:** `gitnexus --help`
- **Cypher Reference:** Run `gitnexus_cypher query="CALL db.schema()"`

## Integration with ClawMind

When working with a codebase, the skill automatically:
1. Indexes the repository
2. Extracts key architectural insights
3. Updates ClawMind knowledge graph with:
   - Project structure
   - Key abstractions
   - Dependency relationships
   - Critical execution paths

This creates persistent code intelligence that survives across sessions.

---

**Version:** 1.0.0  
**GitNexus Version:** Compatible with 1.5.x  
**License:** MIT (skill), PolyForm-Noncommercial (GitNexus OSS)
