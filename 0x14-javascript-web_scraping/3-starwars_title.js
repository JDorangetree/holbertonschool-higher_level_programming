#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + args[2] + '/',
  method: 'GET'
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
