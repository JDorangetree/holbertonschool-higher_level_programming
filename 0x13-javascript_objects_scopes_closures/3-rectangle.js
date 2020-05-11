#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const X = 'X';
    for (let i = this.height; i > 0; i--) {
      console.log(X.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
