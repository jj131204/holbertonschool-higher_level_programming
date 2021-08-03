#!/usr/bin/node
// add
const myVar = parseInt(process.argv[2]);
const myVar1 = parseInt(process.argv[3]);

add(myVar, myVar1);

function add (a, b) {
  console.log(a + b);
}
