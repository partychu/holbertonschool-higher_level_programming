#!/usr/bin/node
const myArgs = process.argv.slice(2);
const request = require('request');

const id = myArgs[0];

request('https://swapi-api.hbtn.io/api/films/' + id, function (error, response, body) {
  if (error) console.error('error:', error);
  const parseBody = JSON.parse(body);
  console.log(parseBody.title);
});
