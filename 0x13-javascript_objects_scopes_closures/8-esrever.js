#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const listLength = list.length;
  for (let i = 0; i < listLength; i++) {
    const reverseItem = list.reduceRight(myFunction);
    newList.push(reverseItem);
    list.pop();
  }
  return newList;
  function myFunction (value) {
    return value;
  }
};
