const PINK = '\x1b[38;5;213m';
const PINK_BOLD = '\x1b[1;38;5;213m';
const WHITE = '\x1b[37m';
const WHITE_BOLD = '\x1b[1;37m';
const RESET = '\x1b[0m';

console.log('\n');

// Option 1: VIVID with pink dot on same line
console.log(WHITE_BOLD + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + PINK_BOLD + '●' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET);
console.log(WHITE_BOLD + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET);

console.log('\n');

// Option 2: VIVID with pink dot offset right
console.log(WHITE_BOLD + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + RESET + '     ' + PINK_BOLD + '●' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET);
console.log(WHITE_BOLD + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET);

console.log('\n');

// Option 3: Two dots above (like the i's in logo)
console.log(WHITE_BOLD + '  ●      ●' + RESET);
console.log(WHITE_BOLD + ' ██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + PINK_BOLD + '●' + RESET);
console.log(WHITE_BOLD + ' ██║   ██║██║██║   ██║██║██╔══██╗' + RESET);
console.log(WHITE_BOLD + ' ██║   ██║██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + ' ╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + '  ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET);
console.log(WHITE_BOLD + '   ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET);

console.log('\n');

// Option 4: Minimal clean
console.log(WHITE_BOLD + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET);
console.log(WHITE_BOLD + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET);
console.log(WHITE_BOLD + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + PINK_BOLD + '  ●' + RESET);

console.log('\n');

// Option 5: Bigger dot
console.log(WHITE_BOLD + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + RESET + PINK_BOLD + '  ██████╗ ' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET + PINK_BOLD + ' ██╔════╝ ' + RESET);
console.log(WHITE_BOLD + '██║   ██║██║██║   ██║██║██║  ██║' + RESET + PINK_BOLD + ' ██║  ██╗ ' + RESET);
console.log(WHITE_BOLD + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET + PINK_BOLD + ' ██║  ╚═╝ ' + RESET);
console.log(WHITE_BOLD + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET + PINK_BOLD + ' ╚██████╗ ' + RESET);
console.log(WHITE_BOLD + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + PINK_BOLD + '  ╚═════╝ ' + RESET);

console.log('\n');
