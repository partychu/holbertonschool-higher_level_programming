#!/usr/bin/node

const arg = process.argv.slice(2);

if (isNaN(arg[0])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < parseInt(arg[0]); x++) {
    for (let y = 0; y < parseInt(arg[0]); y++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
