#!/usr/bin/node
//  reads and prints the content of a file

const argv1 = process.argv[2];

const https = require('https');

https.get(argv1, function (res) {
  console.log('code:', res.statusCode);
}).on('error', function (e) {
  console.error(e);
});
