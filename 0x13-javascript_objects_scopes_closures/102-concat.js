#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const [,, file1, file2, destination] = process.argv;

try {
  const content1 = fs.readFileSync(file1, 'utf-8');
  const content2 = fs.readFileSync(file2, 'utf-8');
  fs.writeFileSync(destination, content1 + content2);
  console.log('Concatenation successful!');
} catch (err) {
  console.error('Error:', err.message);
}

