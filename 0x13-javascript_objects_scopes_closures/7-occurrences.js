#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(myFunction);
  return newList.length;

  function myFunction (value) {
    return value === searchElement;
  }
};
