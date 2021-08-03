#!/usr/bin/node
// parseInt
const myVar = parseInt(process.argv[2]);
if (isNaN(myVar)) {
  console.log('Not a number');
}
else {
  console.log(myVar);
}
