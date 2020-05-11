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

  rotate () {
    const newWidth = this.height;
    this.height = this.width;
    this.width = newWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

module.exports = Rectangle;
