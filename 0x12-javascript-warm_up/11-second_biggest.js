#!/usr/bin/node
const args = process.argv;
const numList = [];
function compare (a, b) {
  return a - b;
}
for (let i = 2; args[i]; i++) {
  numList.push(parseInt(args[i]));
}
if (args.length <= 3) {
  console.log(0);
} else {
  numList.sort(compare).reverse();
  console.log(numList[1]);
}
