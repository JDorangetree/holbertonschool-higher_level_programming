#!/usr/bin/node
const process = require('process');
const args = process.argv;
const nArgs = args.length;
if (nArgs === 2) {
  console.log('No argument');
} else if (nArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
