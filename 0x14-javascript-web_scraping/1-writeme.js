#!/usr/bin/node

const file = process.argv[2];
const data = process.argv[3];
const codi = 'utf8';
const fs = require('fs');

fs.writeFile(file, data, codi, function (err) {
  if (err) {
    console.log(err);
  }
});
