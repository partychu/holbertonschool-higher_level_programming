#!/usr/bin/node

const arg = process.argv.slice(2);

function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return parseInt(a) + parseInt(b);
  }
}

console.log(add(arg[0], arg[1]));
