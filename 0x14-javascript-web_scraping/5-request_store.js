#!/usr/bin/node
//  reads and prints the content of a file

const argv1 = process.argv[2];
const argv2 = process.argv[3];
const fs = require('fs');

const request = require('request');

request(argv1, function (err, res, body) {
  if (err) {
    console.log(err);
  }

  fs.writeFile(argv2, body, err => {
    if (err) {
      console.error(err);
    }
  });
});
