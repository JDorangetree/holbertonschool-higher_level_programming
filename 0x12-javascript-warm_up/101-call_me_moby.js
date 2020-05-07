#!/usr/bin/node
exports.callMeMoby = function callMeMoby (x, theFunction) {
  let i = 0;
  while (i < x) {
    theFunction.call();
    ++i;
  }
};
