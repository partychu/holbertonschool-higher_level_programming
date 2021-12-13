#!/usr/bin/node

const args = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(args));
