#!/usr/bin/node
const myArg = process.argv;

if (myArg.length <= 3) {
  console.log(0);
} else {
  const list = myArg.sort();
  console.log(list.reverse()[1]);
}
