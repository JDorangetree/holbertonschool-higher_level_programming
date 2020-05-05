#!/usr/bin/node
const process = require('process');
const args = process.argv;
let args1 = 'undefined';
let args2 = 'undefined';
const nArgs = args.length;
if (nArgs === 3) {
  args1 = args[2];
} else {
  args1 = args[2];
  args2 = args[3];
}
console.log(args1 + ' is ' + args2);
