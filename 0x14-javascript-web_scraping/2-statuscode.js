#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET'
};

request(options, function (res, error) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', res && res.statusCode);
  }
});
