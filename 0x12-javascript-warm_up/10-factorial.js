#!/usr/bin/node
const args = process.argv;
let numPrint;
function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return factorial(x - 1) * x;
  }
}
if (args[2] === undefined || !parseInt(args[2])) {
  console.log(1);
} else {
  numPrint = factorial(parseInt(args[2]));
  console.log(numPrint);
}
