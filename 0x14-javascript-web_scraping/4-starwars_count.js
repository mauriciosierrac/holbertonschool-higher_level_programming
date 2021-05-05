#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    const id = /18/;
    for (let i = 0; i < data.length; i++) {
      const charData = data[i].characters;
      for (let j = 0; j < charData.length; j++) {
        if (id.test(charData[j]) === true) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
