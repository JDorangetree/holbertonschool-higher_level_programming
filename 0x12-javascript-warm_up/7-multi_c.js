#!/usr/bin/node
const process = require('process');
const args = process.argv;
const myText = 'C is fun';
let i = 0;
let z;
const nArgs = args.length;
if (nArgs === 2) {
  console.log('Missing number of occurrences');
} else {
  z = args[2];
  while (i < z) {
    console.log(myText);
    i++;
  }
}
