#!/usr/bin/node
// square
const Rectangle = require('./5-square');

class Square extends Rectangle {

  constructor (size) {
    super(size, size);
  }
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let count;
    for (count = 0; count < this.height; count++) {
       console.log(c .repeat(this.width));
    }

  }
}
module.exports = Square;
