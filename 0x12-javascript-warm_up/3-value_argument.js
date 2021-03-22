#!/usr/bin/node
const myArg = process.argv;
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(myArg[2]);
}
