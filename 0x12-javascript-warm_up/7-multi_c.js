#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num) || num <= 0) {
  console.log('Missing number of occurrences');
} else {
  const absNum = Math.abs(num); // Convert negative number to its absolute value
  for (let i = 0; i < absNum; i++) {
    console.log('C is fun');
  }
}

