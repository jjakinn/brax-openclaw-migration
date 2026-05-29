# GitNexus Skill Examples

## Example 1: Explore a New Codebase

When you need to understand an unfamiliar codebase quickly:

```xml
<!-- Step 1: Index the repository -->
<gitnexus_analyze path="~/projects/world-monitor" embeddings="true" />

<!-- Step 2: Search for authentication logic -->
<gitnexus_query query="how does user authentication work" limit="5" />

<!-- Step 3: Get full context of a key function -->
<gitnexus_context name="VideoPanel" type="class" />

<!-- Step 4: Check what depends on it -->
<gitnexus_impact target="VideoPanel" direction="upstream" depth="2" />
```

## Example 2: Safe Refactoring

Before renaming a function or class:

```xml
<!-- Step 1: Analyze blast radius -->
<gitnexus_impact target="oldFunctionName" direction="upstream" depth="3" />

<!-- Step 2: Preview rename changes -->
<gitnexus_rename symbol_name="oldFunctionName" new_name="newFunctionName" dry_run="true" />

<!-- Step 3: If preview looks good, apply changes -->
<gitnexus_rename symbol_name="oldFunctionName" new_name="newFunctionName" dry_run="false" />
```

## Example 3: Pre-commit Validation

Check the impact of your changes before committing:

```xml
<!-- Step 1: Detect what changed -->
<gitnexus_detect_changes scope="staged" />

<!-- Step 2: For each important changed symbol, check impact -->
<gitnexus_impact target="changedFunction" direction="upstream" depth="2" />

<!-- Step 3: Re-index after commit to keep knowledge graph fresh -->
<gitnexus_analyze force="true" />
```

## Example 4: Complex Query with Cypher

Use raw Cypher queries for custom analysis:

```xml
<!-- Find all functions related to authentication -->
<gitnexus_cypher query="MATCH (c:Community)<-[:MEMBER_OF]-(fn:Function) WHERE c.heuristicLabel = 'Authentication' RETURN fn.name, fn.filePath" />

<!-- Find functions with no callers (dead code candidates) -->
<gitnexus_cypher query="MATCH (f:Function) WHERE NOT (f)<-[:CALLS]-() RETURN f.name, f.filePath" />

<!-- Find circular dependencies -->
<gitnexus_cypher query="MATCH path = (a)-[:CALLS*2..5]->(a) RETURN path LIMIT 5" />
```

## Example 5: Multi-repo Analysis

For microservices or monorepos:

```xml
<!-- Create a repository group -->
<gitnexus_analyze path="~/projects/api-gateway" />
<gitnexus_analyze path="~/projects/auth-service" />

<!-- CLI commands for group management (run in terminal) -->
gitnexus group create backend-services
gitnexus group add backend-services api-gateway
gitnexus group add backend-services auth-service
gitnexus group sync backend-services

<!-- Query across all repos in the group -->
gitnexus group query backend-services "login flow"
```

## Example 6: Generate Documentation

Create wiki from knowledge graph:

```xml
<!-- Generate auto-updating documentation -->
<gitnexus_wiki model="gpt-4o-mini" />

<!-- With custom model -->
<gitnexus_wiki model="claude-3-5-sonnet" base_url="https://api.anthropic.com/v1" />
```

## Real-World Session Flow

Here's how a typical coding session with GitNexus might look:

### 1. Start of Session
```
<gitnexus_status />
→ Shows index is 3 days old

<gitnexus_analyze force="true" />
→ Re-indexes current repo
```

### 2. Understanding a Bug
```
<gitnexus_query query="error handling in auth middleware" />
→ Finds relevant functions

<gitnexus_context name="handleAuthError" />
→ Shows full context: callers, callees, processes

<gitnexus_impact target="handleAuthError" direction="upstream" depth="3" />
→ Shows 12 functions that could be affected by changes
```

### 3. Making Changes
```
<gitnexus_detect_changes scope="unstaged" />
→ Shows what files are modified

<!-- Make edits in editor -->

<gitnexus_impact target="modifiedFunction" direction="upstream" />
→ Validates changes are safe
```

### 4. Before Commit
```
<gitnexus_detect_changes scope="staged" />
→ Final check of what's being committed

<git commit -m "fix: handle edge case in auth">

<gitnexus_analyze />
→ Update index with new commit
```

## Tips for Best Results

1. **Index with embeddings** for semantic search
   ```xml
   <gitnexus_analyze embeddings="true" />
   ```

2. **Generate skills** for complex codebases
   ```xml
   <gitnexus_analyze skills="true" />
   ```

3. **Use impact analysis** before any refactor
   ```xml
   <gitnexus_impact target="functionName" depth="3" />
   ```

4. **Keep index fresh** after significant changes
   ```xml
   <gitnexus_analyze force="true" />
   ```

5. **Dry run first** for renames
   ```xml
   <gitnexus_rename symbol_name="old" new_name="new" dry_run="true" />
   ```

## Integration with ClawMind

When working with a codebase:

1. GitNexus provides **structural intelligence**
   - Call graphs
   - Dependencies
   - Impact analysis

2. ClawMind provides **semantic intelligence**
   - What the code does
   - Why decisions were made
   - Historical context

Together they give you **complete codebase awareness**.

Example workflow:
```
<!-- Get structural context -->
<gitnexus_context name="VideoPanel" />

<!-- Get semantic context from memory -->
Check ClawMind: VideoPanel.md

<!-- Make informed changes -->
Now you know both HOW it works (GitNexus) and WHY it works that way (ClawMind)
```
