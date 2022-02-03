#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (error) console.error('error:', error);
  const obj = JSON.parse(body);
  const result = {};
  for (const todo of obj) {
    if (todo.completed) {
      if (result[todo.userId]) { result[todo.userId]++; }
    } else {
      result[todo.userId] = 1;
    }
  }
  console.log(result);
});
