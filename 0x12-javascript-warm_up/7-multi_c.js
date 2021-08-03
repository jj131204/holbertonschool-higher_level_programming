#!/usr/bin/node
// c is fun
const myVar = 'C is fun';
const arg = parseInt(process.argv[2]);
let count;
for (count = 0; count <= arg; count++) {
  console.log(myVar);
}
