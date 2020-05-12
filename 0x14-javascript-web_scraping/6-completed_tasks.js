#!/usr/bin/node
const request = require('request');
const args = process.argv;
const returnDict = {};
const options = {
  url: args[2]
};
request(options, function (error, response, body) {
  if (!error === null) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    const ids = [];
    for (let i = 0; i < json.length; i++) {
      ids.push(json[i].userId);
    }
    const uniOcurr = Array.from(new Set(ids));
    for (let b = 0; b < uniOcurr.length; b++) {
      let count = 0;
      for (let a = 0; a < json.length; a++) {
        if (json[a].userId === uniOcurr[b]) {
          if (json[a].completed === true) {
            count++;
          }
        }
      }
      returnDict[uniOcurr[b]] = count;
    }
  }
  console.log(returnDict);
});
