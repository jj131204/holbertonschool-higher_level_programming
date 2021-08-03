#!/usr/bin/node
// defining  class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let count;
    for (count = 0; count < this.height; count++) {
       console.log('X'.repeat(this.width));
    }
  }


  rotate() {
    this.width = this.height;
    this.height = this.width;
  }

  double() {
    this.width = this.width * 2;
    this.height = this.height * 2;
 }

}
module.exports = Rectangle;
