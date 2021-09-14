#!/usr/bin/node
//  reads and prints the content of a file

const argv1 = process.argv[2];
const argv2 =  process.argv[3];


const fs = require('fs');

fs.appendFile(argv1, argv2, function (err) {
  if (err) {
    console.log('error: ', err);
    // append failed
  } else {
    // done
  }
});
