#!/usr/bin/node
fs = require('fs');

fs.readFile('cisfun', 'utf8', (err,data) => {
	if (err) throw err;
	console.log(data);
});
