#!/usr/bin/node

const numString = process.argv[2];

if (!numString.match(/^[-]?[0-9]+$/)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(numString);
  const absNum = Math.abs(num);
  for (let i = 0; i < absNum; i++) {
    console.log('C is fun');
  }
}

