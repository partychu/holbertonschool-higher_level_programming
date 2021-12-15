#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let n = 0;
  for (const o in list) {
    if (list[o] === searchElement) {
      n++;
    }
  }
  return n;
};
