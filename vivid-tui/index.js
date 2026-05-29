#!/usr/bin/env node
/**
 * 🦆 VIVID Agent Terminal UI
 * Branded wrapper around OpenClaw's built-in TUI
 * 
 * Usage:
 *   npx vivid-tui          # Connect to running gateway
 *   npx vivid-tui --start  # Start gateway if not running, then connect
 */

const { spawn, execSync } = require('child_process');
const readline = require('readline');
const fs = require('fs');
const path = require('path');

const { getVividBanner, printBanner, printConnecting, printConnected, printError, printInfo, formatUserMessage, formatAgentMessage, formatThinking } = require('./banner');

const GATEWAY_PORT = 18789;
const GATEWAY_URL = `http://localhost:${GATEWAY_PORT}`;

// Check if gateway is running
function isGatewayRunning() {
  try {
    execSync(`curl -s -o /dev/null -w "%{http_code}" ${GATEWAY_URL}/status`, { timeout: 3000 });
    return true;
  } catch {
    return false;
  }
}

// Start gateway in background
function startGateway() {
  printInfo('Starting OpenClaw gateway...');
  const gateway = spawn('openclaw', ['gateway', 'start'], {
    detached: true,
    stdio: 'ignore'
  });
  gateway.unref();
  printInfo(`Gateway started (PID: ${gateway.pid})`);
}

// Simple chat mode (fallback when openclaw tui isn't available)
async function simpleChatMode() {
  printBanner();
  printInfo(`Connecting to ${GATEWAY_URL}`);
  
  // Try to use openclaw tui
  try {
    execSync('which openclaw', { stdio: 'ignore' });
    printConnected();
    printInfo('Launching OpenClaw TUI...\n');
    
    const tui = spawn('openclaw', ['tui'], {
      stdio: 'inherit'
    });
    
    tui.on('exit', (code) => {
      process.exit(code);
    });
    
    return;
  } catch {
    // openclaw not in PATH, use simple mode
  }
  
  printError('OpenClaw TUI not available. Using simple chat mode.');
  printInfo('For full TUI experience, run: npm install -g openclaw');
  console.log('');
  
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    prompt: '\x1b[38;5;201m\x1b[1mVIVID> \x1b[0m'
  });
  
  console.log(formatAgentMessage('Hello! I am VIVID, your AI agent. How can I help you today?'));
  console.log('');
  
  rl.prompt();
  
  rl.on('line', (input) => {
    const text = input.trim();
    if (!text) {
      rl.prompt();
      return;
    }
    
    if (text === '/quit' || text === '/exit' || text === '/q') {
      console.log('\n\x1b[38;5;245m👋 Goodbye from VIVID!\x1b[0m\n');
      rl.close();
      return;
    }
    
    if (text === '/help' || text === '/h') {
      console.log('');
      console.log('\x1b[38;5;33m\x1b[1mVIVID Commands:\x1b[0m');
      console.log('  /help, /h     Show this help');
      console.log('  /quit, /q     Exit VIVID');
      console.log('  /clear, /c    Clear screen');
      console.log('  /status        Check gateway status');
      console.log('');
      rl.prompt();
      return;
    }
    
    if (text === '/clear' || text === '/c') {
      console.clear();
      printBanner();
      rl.prompt();
      return;
    }
    
    if (text === '/status') {
      const running = isGatewayRunning();
      console.log(`\n  Gateway: ${running ? '\x1b[38;5;82mRunning\x1b[0m' : '\x1b[38;5;196mNot Running\x1b[0m'}`);
      console.log(`  URL: ${GATEWAY_URL}\n`);
      rl.prompt();
      return;
    }
    
    console.log('');
    console.log(formatUserMessage(text));
    console.log('');
    console.log(formatThinking());
    
    // Simulate response (in real implementation, this would call the gateway API)
    setTimeout(() => {
      console.log('\r\x1b[K'); // Clear thinking line
      console.log(formatAgentMessage('I received your message. In full mode, I would process this through the OpenClaw gateway. Please install OpenClaw for the complete experience.'));
      console.log('');
      rl.prompt();
    }, 1500);
  });
  
  rl.on('close', () => {
    process.exit(0);
  });
}

// Main
async function main() {
  const args = process.argv.slice(2);
  const shouldStart = args.includes('--start') || args.includes('-s');
  
  // Check if gateway is running
  let running = isGatewayRunning();
  
  if (!running && shouldStart) {
    startGateway();
    printInfo('Waiting for gateway to start...');
    
    // Wait up to 10 seconds for gateway
    for (let i = 0; i < 20; i++) {
      await new Promise(r => setTimeout(r, 500));
      if (isGatewayRunning()) {
        running = true;
        break;
      }
    }
  }
  
  if (!running) {
    printBanner();
    printError(`OpenClaw gateway not running at ${GATEWAY_URL}`);
    printInfo('Start it with: openclaw gateway start');
    printInfo('Or run with --start flag: npx vivid-tui --start');
    console.log('');
    process.exit(1);
  }
  
  // Launch TUI
  await simpleChatMode();
}

main().catch(err => {
  printError(err.message);
  process.exit(1);
});
