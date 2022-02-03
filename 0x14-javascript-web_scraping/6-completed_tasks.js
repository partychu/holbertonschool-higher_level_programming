#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (error) console.error('error:', error);
  const todo = JSON.parse(body);
  const result = {};
  for (const t of todo) {
    if (t.completed) {
      if (result[t.userId] === undefined) {
        result[t.userId] = 1;
      } else {
        result[t.userId] += 1;
      }
    }
  }
  console.log(result);
});
