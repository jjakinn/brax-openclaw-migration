const WHITE = '\u001b[1;37m';
const PINK = '\u001b[1;38;5;213m';
const RESET = '\u001b[0m';

// Option 1: Pink dot inline
console.log('\n=== Option 1: Pink dot inline ===');
process.stdout.write(WHITE + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + PINK + '●' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET + '\n');
process.stdout.write(WHITE + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + '\n');

// Option 2: White dots above i's + pink dot at end
console.log('\n=== Option 2: White dots above i\'s + pink dot at end ===');
process.stdout.write(WHITE + '  ●      ●' + RESET + '\n');
process.stdout.write(WHITE + ' ██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + PINK + '●' + RESET + '\n');
process.stdout.write(WHITE + ' ██║   ██║██║██║   ██║██║██╔══██╗' + RESET + '\n');
process.stdout.write(WHITE + ' ██║   ██║██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + ' ╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + '  ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET + '\n');
process.stdout.write(WHITE + '   ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + '\n');

// Option 3: Pink dot offset right
console.log('\n=== Option 3: Pink dot offset right ===');
process.stdout.write(WHITE + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + RESET + '     ' + PINK + '●' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET + '\n');
process.stdout.write(WHITE + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + '\n');

// Option 4: Pink dot bottom right
console.log('\n=== Option 4: Pink dot bottom right ===');
process.stdout.write(WHITE + '██╗   ██╗██╗██╗   ██╗██╗██████╗ ' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██╔══██╗' + RESET + '\n');
process.stdout.write(WHITE + '██║   ██║██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + '╚██╗ ██╔╝██║██║   ██║██║██║  ██║' + RESET + '\n');
process.stdout.write(WHITE + ' ╚████╔╝ ██║╚██████╔╝██║██████╔╝' + RESET + '\n');
process.stdout.write(WHITE + '  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ ' + RESET + PINK + '  ●' + RESET + '\n');

console.log('\n');
