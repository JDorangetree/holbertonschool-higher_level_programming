#!/usr/bin/node
exports.logMe = function (item) {
  if (this.index === undefined) {
    this.index = 0;
  }
  console.log(`${this.index}: ${item}`);
  this.index++;
};
