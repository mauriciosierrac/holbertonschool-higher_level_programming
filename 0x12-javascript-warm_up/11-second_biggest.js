#!/usr/bin/node
const myArg = process.argv
if (myArg.length <= 3) {
  console.log(0);
} else {
  const list = myArg
    .slice(2, myArg.length)
    .map(Number)
    .sort()
    .reverse();
  console.log(list[1]);
}
