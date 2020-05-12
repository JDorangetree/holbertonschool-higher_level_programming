#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET'
};
request(options, function (error, response) {
  if (response) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(error);
  }
});
