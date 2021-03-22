#!/usr/bin/node
const num = process.argv[2];
let i;
if (num === undefined || isNaN(num)) {
  console.log('Missing size');
} else {
  for (i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
