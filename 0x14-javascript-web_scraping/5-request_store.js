#!/usr/bin/node
const request = require('request');
const args = process.argv;
const fs = require('fs');
const options = {
  url: args[2]
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.log(error);
  } else {
    fs.writeFile(`${args[3]}`, body, 'utf-8', (error) => {
      if (error) {
        return console.log(error);
      }
    });
  }
});
