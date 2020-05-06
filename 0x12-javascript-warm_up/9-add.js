#!/usr/bin/node
const process = require('process');
const args = process.argv;
const nArgs = args.length;
if (nArgs === 2 || nArgs === 3) {
  console.log('NaN');
} else {
  console.log(parseInt(args[2]) + parseInt(args[3]));
}
