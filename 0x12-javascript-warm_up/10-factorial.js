#!/usr/bin/node
const process = require('process');
const args = process.argv;
const nArgs = args.length;
let x;
function factorial (number) {
  let result = 1;
  while (number > 0) {
    result = number * result;
    number--;
  }
  return (result);
}
if (nArgs === 2) {
  console.log('1');
} else {
  x = factorial(args[2]);
  console.log(x);
}
