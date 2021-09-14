#!/usr/bin/node
//  reads and prints the content of a file

const url = process.argv[2];
const request = require('request');

request(url, function (err, result, body) {
  console.log('code: ' + result.statusCode);
  if (err) {
    console.log(err);
  }
});
