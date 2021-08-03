#!/usr/bin/node
// x
const myVar = 'X';
const arg = parseInt(process.argv[2]);
let count;
if (isNaN(arg)) {
  console.log('Missing size');
}
else {
  for (count = 0; count < arg; count++) {
    console.log(myVar.repeat(arg));

  }
}
