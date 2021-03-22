#!/usr/bin/node
const myArg = process.argv[2];
if (myArg === undefined || isNaN(myArg)) {
  console.log('Not a number');
} else if (parseInt(myArg)) {
  console.log('My number: ' + parseInt(myArg));
}
