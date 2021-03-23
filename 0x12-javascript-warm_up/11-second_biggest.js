#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv
    .map(Number)
    .slice(2, process.argv.length)
    .sort(function (a, b) {
      return b - a;
    });
  console.log(parseInt(list[1]));
}
