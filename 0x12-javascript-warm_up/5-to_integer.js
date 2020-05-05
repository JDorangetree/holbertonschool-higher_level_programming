#!/usr/bin/node
const process = require('process');
const args = process.argv;
const nArgs = args.length;
let myNumber;
if (nArgs === 2) {
  console.log('Not a number');
} else {
  myNumber = parseInt(args[2]);
  if (Number.isNaN(myNumber)) {
    console.log('Not a number');
  } else {
    console.log('My number: ' + myNumber);
  }
}
