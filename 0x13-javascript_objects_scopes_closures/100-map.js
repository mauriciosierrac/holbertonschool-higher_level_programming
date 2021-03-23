#!/usr/bin/node
const array = require('./100-data.js');
const map1 = array.list.map((a, b) => a * b);

console.log(array.list);
console.log(map1);
