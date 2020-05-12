#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: args[2]
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.log(error);
  } else {
    let count = 0;
    let result = [];
    const json = JSON.parse(body);
    result = json.results;
    for (let i = 0; i < result.length; i++) {
      let characters = [];
      characters = (result[i].characters);
      for (let a = 0; a < characters.length - 1; a++) {
        if (characters[a] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
