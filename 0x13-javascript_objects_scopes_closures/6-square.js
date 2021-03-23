#!/usr/bin/node
const SquareTwo = require('./5-square.js');

module.exports = class Square extends SquareTwo {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
