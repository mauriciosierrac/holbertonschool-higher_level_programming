#!/usr/bin/node
const myArg = process.argv;
if (process.argv[2] === undefined) {
  console.log('No arguments');
} else {
  console.log(myArg[2]);
}
