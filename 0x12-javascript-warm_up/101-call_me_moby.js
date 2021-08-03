#!/usr/bin/node
// x times
exports.callMeMoby = function (x, theFunction) {
  let count;
  for (count = 0; count < x; count++) {
    theFunction();
  }
};
