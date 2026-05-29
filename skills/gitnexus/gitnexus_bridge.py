#!/usr/bin/env python3
"""
GitNexus Skill Bridge for OpenClaw
Integrates GitNexus code intelligence with OpenClaw agent framework
"""

import subprocess
import json
import os
import sys
import argparse
from pathlib import Path
from typing import Optional, Dict, Any, List

class GitNexusBridge:
    """Bridge between OpenClaw and GitNexus CLI/API"""
    
    def __init__(self):
        self.gitnexus_path = self._find_gitnexus()
        self.api_url = os.environ.get('GITNEXUS_API_URL', 'http://localhost:3001')
        
    def _find_gitnexus(self) -> Optional[str]:
        """Find gitnexus binary in PATH or environment"""
        # Check environment override first
        if env_path := os.environ.get('GITNEXUS_PATH'):
            if Path(env_path).exists():
                return env_path
        
        # Check common locations
        candidates = [
            os.path.expanduser('~/gitnexus/gitnexus/dist/cli/index.js'),  # Local build (priority)
            'gitnexus',
            os.path.expanduser('~/.npm-global/bin/gitnexus'),
            '/usr/local/bin/gitnexus',
            '/opt/homebrew/bin/gitnexus',
        ]
        
        for candidate in candidates:
            try:
                result = subprocess.run(
                    [candidate, '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0:
                    return candidate
            except (subprocess.TimeoutExpired, FileNotFoundError):
                continue
        
        return None
    
    def _run_cli(self, args: List[str], cwd: Optional[str] = None) -> Dict[str, Any]:
        """Run gitnexus CLI command and return structured output"""
        if not self.gitnexus_path:
            return {
                'success': False,
                'error': 'GitNexus not found. Install with: npm install -g gitnexus'
            }
        
        cmd = [self.gitnexus_path] + args
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=cwd or os.getcwd(),
                timeout=300  # 5 min timeout for indexing
            )
            
            # Try to parse JSON output
            if result.stdout:
                try:
                    return {
                        'success': result.returncode == 0,
                        'data': json.loads(result.stdout),
                        'raw': result.stdout
                    }
                except json.JSONDecodeError:
                    return {
                        'success': result.returncode == 0,
                        'raw': result.stdout,
                        'error': result.stderr if result.stderr else None
                    }
            else:
                return {
                    'success': result.returncode == 0,
                    'raw': result.stdout,
                    'error': result.stderr if result.stderr else None
                }
                
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'error': 'Command timed out after 5 minutes'
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def version(self) -> Dict[str, Any]:
        """Get GitNexus version"""
        return self._run_cli(['--version'])
    
    def analyze(self, path: str = '.', force: bool = False, 
                embeddings: bool = True, skills: bool = False,
                skip_agents_md: bool = False) -> Dict[str, Any]:
        """Index a repository"""
        args = ['analyze', path]
        
        if force:
            args.append('--force')
        if embeddings:
            args.append('--embeddings')
        if skills:
            args.append('--skills')
        if skip_agents_md:
            args.append('--skip-agents-md')
        
        return self._run_cli(args, cwd=path if os.path.isdir(path) else os.path.dirname(path))
    
    def list_repos(self) -> Dict[str, Any]:
        """List all indexed repositories"""
        return self._run_cli(['list'])
    
    def status(self, repo: Optional[str] = None) -> Dict[str, Any]:
        """Check index status"""
        args = ['status']
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def clean(self, repo: Optional[str] = None, all_repos: bool = False) -> Dict[str, Any]:
        """Clean/delete index"""
        args = ['clean']
        if all_repos:
            args.extend(['--all', '--force'])
        elif repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def query(self, query: str, repo: Optional[str] = None, 
              limit: int = 10) -> Dict[str, Any]:
        """Search the knowledge graph"""
        # Use gitnexus query command
        args = ['query', query, '--limit', str(limit)]
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def context(self, name: str, repo: Optional[str] = None,
                type_hint: Optional[str] = None) -> Dict[str, Any]:
        """Get 360-degree symbol context"""
        args = ['mcp', 'context', name]
        if repo:
            args.extend(['--repo', repo])
        if type_hint:
            args.extend(['--type', type_hint])
        return self._run_cli(args)
    
    def impact(self, target: str, direction: str = 'upstream',
               depth: int = 2, min_confidence: float = 0.8,
               repo: Optional[str] = None) -> Dict[str, Any]:
        """Blast radius analysis"""
        args = [
            'mcp', 'impact', target,
            '--direction', direction,
            '--depth', str(depth),
            '--min-confidence', str(min_confidence)
        ]
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def detect_changes(self, scope: str = 'all', 
                       repo: Optional[str] = None) -> Dict[str, Any]:
        """Git-diff impact analysis"""
        args = ['mcp', 'detect-changes', '--scope', scope]
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def cypher(self, query: str, repo: Optional[str] = None) -> Dict[str, Any]:
        """Raw Cypher graph query"""
        args = ['mcp', 'cypher', query]
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def rename(self, symbol_name: str, new_name: str,
               dry_run: bool = True, repo: Optional[str] = None) -> Dict[str, Any]:
        """Multi-file coordinated rename"""
        args = ['mcp', 'rename', symbol_name, new_name]
        if dry_run:
            args.append('--dry-run')
        if repo:
            args.extend(['--repo', repo])
        return self._run_cli(args)
    
    def wiki(self, repo: Optional[str] = None, model: str = 'gpt-4o-mini',
             base_url: Optional[str] = None) -> Dict[str, Any]:
        """Generate repository wiki"""
        args = ['wiki']
        if repo:
            args.extend(['--repo', repo])
        if model:
            args.extend(['--model', model])
        if base_url:
            args.extend(['--base-url', base_url])
        return self._run_cli(args)
    
    def serve(self, port: int = 3001) -> Dict[str, Any]:
        """Start HTTP server (background)"""
        # This would need to be run differently - async/background
        args = ['serve', '--port', str(port)]
        return self._run_cli(args)


def main():
    """CLI entry point for OpenClaw tool calls"""
    parser = argparse.ArgumentParser(description='GitNexus Skill Bridge')
    parser.add_argument('action', choices=[
        'version', 'analyze', 'list', 'status', 'clean',
        'query', 'context', 'impact', 'detect-changes',
        'cypher', 'rename', 'wiki', 'serve'
    ])
    
    # Common args
    parser.add_argument('--repo', '-r', help='Repository name')
    parser.add_argument('--path', '-p', default='.', help='Repository path')
    
    # Analyze args
    parser.add_argument('--force', action='store_true', help='Force re-index')
    parser.add_argument('--embeddings', action='store_true', default=True, help='Generate embeddings')
    parser.add_argument('--skills', action='store_true', help='Generate skill files')
    parser.add_argument('--skip-agents-md', action='store_true', help='Skip AGENTS.md')
    
    # Query args
    parser.add_argument('--query', '-q', help='Search query')
    parser.add_argument('--limit', '-l', type=int, default=10, help='Result limit')
    
    # Context args
    parser.add_argument('--name', '-n', help='Symbol name')
    parser.add_argument('--type', '-t', help='Symbol type')
    
    # Impact args
    parser.add_argument('--target', help='Target symbol')
    parser.add_argument('--direction', default='upstream', choices=['upstream', 'downstream'])
    parser.add_argument('--depth', type=int, default=2)
    parser.add_argument('--min-confidence', type=float, default=0.8)
    
    # Detect changes args
    parser.add_argument('--scope', default='all', choices=['all', 'staged', 'unstaged'])
    
    # Rename args
    parser.add_argument('--symbol-name', help='Symbol to rename')
    parser.add_argument('--new-name', help='New symbol name')
    parser.add_argument('--dry-run', action='store_true', default=True)
    
    # Wiki args
    parser.add_argument('--model', default='gpt-4o-mini')
    parser.add_argument('--base-url', help='API base URL')
    
    # Serve args
    parser.add_argument('--port', type=int, default=3001)
    
    # Clean args
    parser.add_argument('--all', action='store_true', help='Clean all repos')
    
    args = parser.parse_args()
    
    bridge = GitNexusBridge()
    
    # Route to appropriate method
    if args.action == 'version':
        result = bridge.version()
    
    elif args.action == 'analyze':
        result = bridge.analyze(
            path=args.path,
            force=args.force,
            embeddings=args.embeddings,
            skills=args.skills,
            skip_agents_md=args.skip_agents_md
        )
    
    elif args.action == 'list':
        result = bridge.list_repos()
    
    elif args.action == 'status':
        result = bridge.status(repo=args.repo)
    
    elif args.action == 'clean':
        result = bridge.clean(repo=args.repo, all_repos=args.all)
    
    elif args.action == 'query':
        if not args.query:
            print(json.dumps({'success': False, 'error': 'Query required'}))
            sys.exit(1)
        result = bridge.query(query=args.query, repo=args.repo, limit=args.limit)
    
    elif args.action == 'context':
        if not args.name:
            print(json.dumps({'success': False, 'error': 'Symbol name required'}))
            sys.exit(1)
        result = bridge.context(name=args.name, repo=args.repo, type_hint=args.type)
    
    elif args.action == 'impact':
        if not args.target:
            print(json.dumps({'success': False, 'error': 'Target required'}))
            sys.exit(1)
        result = bridge.impact(
            target=args.target,
            direction=args.direction,
            depth=args.depth,
            min_confidence=args.min_confidence,
            repo=args.repo
        )
    
    elif args.action == 'detect-changes':
        result = bridge.detect_changes(scope=args.scope, repo=args.repo)
    
    elif args.action == 'cypher':
        if not args.query:
            print(json.dumps({'success': False, 'error': 'Cypher query required'}))
            sys.exit(1)
        result = bridge.cypher(query=args.query, repo=args.repo)
    
    elif args.action == 'rename':
        if not args.symbol_name or not args.new_name:
            print(json.dumps({'success': False, 'error': 'symbol-name and new-name required'}))
            sys.exit(1)
        result = bridge.rename(
            symbol_name=args.symbol_name,
            new_name=args.new_name,
            dry_run=args.dry_run,
            repo=args.repo
        )
    
    elif args.action == 'wiki':
        result = bridge.wiki(repo=args.repo, model=args.model, base_url=args.base_url)
    
    elif args.action == 'serve':
        result = bridge.serve(port=args.port)
    
    else:
        result = {'success': False, 'error': f'Unknown action: {args.action}'}
    
    # Output as JSON for OpenClaw
    print(json.dumps(result, indent=2))
    sys.exit(0 if result.get('success') else 1)


if __name__ == '__main__':
    main()
