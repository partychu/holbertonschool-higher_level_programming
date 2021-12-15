#!/usr/bin/node

const dict = require('./101-data').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key]] === undefined) { // 1, 2, 1, 3
    newdict[dict[key]] = [];
  }
  newdict[dict[key]].push(key); // 89, 90, 91,
}
