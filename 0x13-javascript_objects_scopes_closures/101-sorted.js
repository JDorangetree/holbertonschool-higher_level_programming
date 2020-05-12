#!/usr/bin/node
const dict = require('./101-data').dict;
const ocurreList = [];
const returnDict = {};
for (const userId in dict) {
  ocurreList.push(dict[userId]);
}
const uniOcurr = Array.from(new Set(ocurreList));
for (let i = 0; i < uniOcurr.length; i++) {
  const listValue = [];
  for (const key in dict) {
    if (uniOcurr[i] === dict[key]) {
      listValue.push(key);
    }
  }
  returnDict[uniOcurr[i]] = listValue;
}
console.log(returnDict);
