#!/usr/bin/node
const request = require('request');
const args = process.argv;
let count = 0;

const options = {
  url: args[2],
  method: 'GET'
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.error(error);
  } else {
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
  }
  console.log(count);
});
