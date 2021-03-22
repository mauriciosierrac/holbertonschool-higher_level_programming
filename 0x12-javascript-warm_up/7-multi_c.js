#!/usr/bin/node
const str = 'C is fun';
const n = process.argv[2];
let i = 0;
if (isNaN(n)) {
  console.log('Missing number of occurrences');
} else {
  while (i < n) {
    console.log(str);
    i++;
  }
}
