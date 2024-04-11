#!/usr/bin/node

const fs = require('fs');

const file1 = process.argv[2];
const file2 = process.argv[3];
const destination = process.argv[4];

const content1 = fs.readFileSync(file1).toString();
const content2 = fs.readFileSync(file2).toString();

fs.writeFileSync(destination, content1 + content2);
