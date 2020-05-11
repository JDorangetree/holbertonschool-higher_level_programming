#!/usr/bin/node
const SquareClass = require('./5-square');

class Square extends SquareClass {
  constructor (w) {
    super(w, w);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = this.height; i > 0; i--) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
