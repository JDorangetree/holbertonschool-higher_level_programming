#!/usr/bin/node
const request = require('request');
const args = process.argv;
let urlList = [];
let results = [];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/'
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    results = json.results;
    urlList = results[args[2] - 1].characters;
    urlList.forEach(element => {
      request(element, function (error, response, body) {
        if (!error === null) {
          console.error(error);
        } else {
          const jsonCha = JSON.parse(body);
          console.log(jsonCha.name);
        }
      });
    });
  }
});
