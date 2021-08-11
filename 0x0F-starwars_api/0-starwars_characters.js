#!/usr/bin/node
const process = require('process');
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;
request(url, 'utf-8', async (err, resp, body) => {
  if (!err) {
    const movie = JSON.parse(body);
    const chars = movie.characters;
    const newPromise = (url) => {
      return new Promise(function (resolve, reject) {
        request(url, 'utf-8', (err, resp, body) => {
          if (err) reject(err);
          else resolve(body);
        });
      });
    };
    for (const each in chars) {
      const actor = await newPromise(chars[each]);
      const charList = JSON.parse(actor);
      console.log(charList.name);
    }
  }
});
