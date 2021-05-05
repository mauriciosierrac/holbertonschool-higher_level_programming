#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const dict = {};
    const data = JSON.parse(body);

    for (let i = 0; i < data.length; i++) {
      if (data[i].completed === true) {
        if (dict[data[i].userId] in data) {
          dict[data[i].userId]++;
        } else {
          dict[data[i].userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
