#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const pathFile = process.argv[3];
const fs = require('fs');
const codi = 'utf8';

request(url, function (body) {
  fs.writeFile(pathFile, body, codi, function (error) {
    if (error) {
      console.log(error);
    } else {
      console.log(url > pathFile);
    }
  });
});
