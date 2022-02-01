#!/usr/bin/node
const fs = require('fs');
const myArgs = process.argv.slice(2);
const request = require('request');

request(myArgs[0], function (error, response, body) {
  if (error) {
    console.error(error);
  }

  fs.writeFile(myArgs[1], body, 'utf-8', err => {
    if (err) {
      console.error(err);
    }
  });
});
