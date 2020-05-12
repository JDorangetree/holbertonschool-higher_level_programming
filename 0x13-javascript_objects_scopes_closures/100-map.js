#!/usr/bin/node
const list = require('./100-data').list;

const factorList = list.map(myFunction, 0);
console.log(list);
console.log(factorList);
function myFunction (value, factor) {
  return value * factor;
}
