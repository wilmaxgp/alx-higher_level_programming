#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 2) {
    return 0;
  }

  arr.sort((a, b) => a - b);
  return arr[arr.length - 2];
}

const args = process.argv.slice(2).map(Number);
console.log(secondBiggest(args));
