#!/usr/bin/node

const arg = process.argv.slice(2);

function factorial (n) {
  if (isNaN(n) || n === 0 || n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(arg[0]));
