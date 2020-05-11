#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const matchList = list.filter(myFunction);
  return matchList.length;

  function myFunction (value) {
    return value === searchElement;
  }
};
