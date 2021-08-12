#!/usr/bin/node

const args = process.argv.slice(2);
const p = parseInt(args[0]);

if (isNaN(p)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + p);
}
