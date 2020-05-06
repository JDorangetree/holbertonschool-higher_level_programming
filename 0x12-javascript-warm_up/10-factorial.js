#!/usr/bin/node
const args = process.argv;
let x = parseInt(args[2]);
let f = 1;
function factorial (number, result) {
  return number * result;
}
while (x > 0) {
  f = factorial(f, x);
  x--;
}
console.log(f);
