#!/usr/bin/node
const process = require('process');
const args = process.argv;
const nArgs = args.length;
const X = 'X';
let square;
if (nArgs === 2 || !Number.isNaN(args[2])) {
  console.log('Missing size');
} else {
  square = args[2];
  while (square > 0) {
    console.log(X.repeat(args[2]));
    square--;
  }
}
