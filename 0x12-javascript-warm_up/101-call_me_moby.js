/*
Defined a function callMeMoby to execute another function x times.
 */
function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = {
  callMeMoby
};
