#!/usr/bin/node
//  reads and prints the content of a file

const argv = process.argv[2];

const fs = require('fs');



fs.readFile(argv, 'utf-8', (err, data) => {
  if(err){
    console.log('error: ', err);
  }
  else {
    console.log(data);
  }
});
