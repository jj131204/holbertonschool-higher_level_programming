#!/usr/bin/node
//  prints the number of arguments
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count = count + 1;
};
