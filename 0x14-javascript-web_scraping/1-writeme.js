#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.writeFile(`${args[2]}`, `${args[3]}`, 'utf-8', function (error) {
  if (error) {
    return console.log(error);
  }
});
