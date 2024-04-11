#!/usr/bin/node

const numString = process.argv[2];

if (!numString || isNaN(numString)) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(numString);
  if (num <= 0) {
    console.log('Missing number of occurrences');
  } else {
    let i = 0;
    while (i < num) {
      console.log('C is fun');
      i++;
    }
  }
}

