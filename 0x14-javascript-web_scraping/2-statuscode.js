#!/usr/bin/node
const request = require('request');
const args = process.argv;

request(`${args[2]}`, function (response) {
  console.log('code:', response && response.code);
});
