#!/usr/bin/node
const fs = require('fs');
const args = process.argv;

fs.writeFile(`${args[2]}`, `${args[3]}\n`, error => {
  if (error) {
    console.log(error);
  }
});
