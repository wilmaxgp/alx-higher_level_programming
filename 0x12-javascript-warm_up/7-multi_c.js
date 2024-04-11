#!/usr/bin/node

const input = process.argv[2];

if (!input || isNaN(input)) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(input);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
