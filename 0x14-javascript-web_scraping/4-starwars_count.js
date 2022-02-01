#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

const url = myArgs[0];
const charID = '18';

request(url, function (error, response, body) {
  if (error) console.error('error:', error);
  const parseBody = JSON.parse(body);
  const starwarsEp = parseBody.results;
  let count = 0;
  for (const i in starwarsEp) {
    for (const c in starwarsEp[i].characters) {
      if (starwarsEp[i].characters[c].includes(charID)) {
        count++;
      }
    }
  }
  console.log(count);
});
