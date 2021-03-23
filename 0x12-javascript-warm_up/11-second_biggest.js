#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort().reverse();
  console.log(parseInt(list[1]));
}
