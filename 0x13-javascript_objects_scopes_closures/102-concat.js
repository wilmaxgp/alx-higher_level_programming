#!/usr/bin/node

const fs = require('fs');

// Check if the correct number of arguments are provided
if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

// Read the contents of the first file
const file1Content = fs.readFileSync(file1Path, 'utf8');

// Read the contents of the second file
const file2Content = fs.readFileSync(file2Path, 'utf8');

// Concatenate the contents of the two files
const concatenatedContent = file1Content + file2Content;

// Write the concatenated content to the destination file
fs.writeFileSync(destinationPath, concatenatedContent);

console.log(`Files ${file1Path} and ${file2Path} concatenated successfully to ${destinationPath}`);

