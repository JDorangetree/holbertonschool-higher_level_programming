#!/usr/bin/node
const request = require('request');
const args = process.argv;
let urlList = [];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + args[2] + '/'
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    urlList = json.characters;
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
