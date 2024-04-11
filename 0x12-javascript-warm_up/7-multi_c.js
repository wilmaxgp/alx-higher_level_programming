#!/usr/bin/node

const numString = process.argv[2];

if (!numString || !numString.match(/^-?\d+$/)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(numString);
  const absNum = Math.abs(num);
  let i = 0;
  while (i < absNum) {
    console.log('C is fun');
    i++;
  }
}

