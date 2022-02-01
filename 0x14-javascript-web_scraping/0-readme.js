#!/usr/bin/node
const myArgs = process.argv.slice(2)
fs = require('fs');

fs.readFile(myArgs[0], 'utf8', function (err,data) {
	if (err) {
	return console.log(err);
	}
	console.log(data);
});
