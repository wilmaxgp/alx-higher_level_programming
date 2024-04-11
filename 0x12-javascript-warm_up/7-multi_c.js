#!/usr/bin/node

const input = process.argv[2];

if (!input || isNaN(input)) {
  console.log('Invalid input. Please provide a valid number.');
} else {
  const count = Number(input);
  let i = 0;
  while (i < count) {
    console.log('Hello world');
    i++;
  }
}

