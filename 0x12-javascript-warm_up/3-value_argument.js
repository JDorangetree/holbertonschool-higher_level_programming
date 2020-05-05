#!/usr/bin/node
const process = require('process');
const args = process.argv;
let x;
let num;
for (x in args) {
  num = x;
}
if (num === '1') {
  console.log('No argument');
} else {
  console.log(args[2]);
}
