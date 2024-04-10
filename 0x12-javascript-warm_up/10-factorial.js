#!/usr/bin/node

function factorial (num) {
  if (num === 0 || num === 1) {
    return 1;
  } else if (num < 0) {
    return Infinity;
  } else {
    return num * factorial(num - 1);
  }
}

const num = parseInt(process.argv[2]);

console.log(factorial(num));
