#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

request(myArgs[0], function (error, response) {
  if (error) console.error('error:', error); // Print the error if one occurred
  console.log('code:', response && response.statusCode);
});
