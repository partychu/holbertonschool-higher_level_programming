#!/usr/bin/node

const n = process.argv.slice(2);

if (n.length <= 1) {
  console.log(0);
} else {
  n.sort((a, b) => a - b);
  console.log(n[n.length - 2]);
}
