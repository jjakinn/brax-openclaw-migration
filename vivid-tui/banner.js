const WHITE_BOLD = '\x1b[1;37m';
const PINK_BOLD = '\x1b[1;38;5;213m';
const RESET = '\x1b[0m';

const VIVID_LOGO = [
  '██╗   ██╗██╗██╗   ██╗██╗██████╗ ',
  '██║   ██║██║██║   ██║██║██╔══██╗',
  '██║   ██║██║██║   ██║██║██║  ██║',
  '╚██╗ ██╔╝██║██║   ██║██║██║  ██║',
  ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝',
  '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ '
];

export function getVividBanner() {
  const lines = [];
  for (let i = 0; i < VIVID_LOGO.length; i++) {
    const line = VIVID_LOGO[i];
    if (i === VIVID_LOGO.length - 1) {
      // Last line: white text + pink dot at bottom right
      lines.push(`${WHITE_BOLD}${line}${RESET}  ${PINK_BOLD}●${RESET}`);
    } else {
      lines.push(`${WHITE_BOLD}${line}${RESET}`);
    }
  }
  return lines.join('\n');
}

export function printBanner() {
  console.log('');
  console.log(getVividBanner());
  console.log('');
  console.log('  \x1b[38;5;213m🎨 VIVID Agent Terminal UI\x1b[0m  \x1b[38;5;245m—  Connected to OpenClaw Gateway\x1b[0m');
  console.log('  \x1b[38;5;245mType your message and press Enter. Use /help for commands.\x1b[0m');
  console.log('');
}

export function printConnecting(gatewayUrl) {
  console.log(`\x1b[38;5;33m⚡ Connecting to ${gatewayUrl}...\x1b[0m`);
}

export function printConnected() {
  console.log('\x1b[38;5;82m✅ Connected!\x1b[0m\n');
}

export function printError(msg) {
  console.log(`\x1b[38;5;196m❌ ${msg}\x1b[0m`);
}

export function printInfo(msg) {
  console.log(`\x1b[38;5;33mℹ️  ${msg}\x1b[0m`);
}

export function formatUserMessage(text) {
  return `\x1b[38;5;201m\x1b[1mYou:\x1b[0m  ${text}`;
}

export function formatAgentMessage(text) {
  return `\x1b[38;5;51m\x1b[1mVIVID:\x1b[0m ${text}`;
}

export function formatThinking() {
  return `\x1b[38;5;245m\x1b[3mVIVID is thinking...\x1b[0m`;
}
