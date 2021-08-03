#!/usr/bin/node
// parseInt
const myVar = process.argv[2];
const integrer = parseInt(myVar);

if (isNaN(integrer)) {
  console.log('no funciono');
} else {
  console.log(myVar);
}
