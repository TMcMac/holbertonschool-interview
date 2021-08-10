#!/usr/bin/node

const args = process.argv;

if (args.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Film Number>');
  process.exit(1);
}

if (Number.isInteger(Number(args[2])) == false) {
  console.log('Usage: ./0-starwars_characters.js <Film Number>');
  process.exit(1);
}

const film = Number(args[2]); // Film number in relase date order
const url = 'https://swapi-api.hbtn.io/api/films/' + film + '/'; // Swapi films base url
const request = require('request');

request(url, function (error, response, body) {
  if (error !== null) {
    console.error('error:', error); // Print the error if one occurred
  }
  if (Number(response.statusCode) !== 200) {
      console.log('statusCode:', response && response.statusCode); // Print the response status code if not an OK
  }

  const payload = JSON.parse(body);
  const characters = payload.characters; // An array of character urls for the SWAPI
  const charDict = {};
  function resolveAfter2Seconds () {
      return new Promise(resolve => {
          setTimeout(() => {
          resolve('resolved');
          }, 2000);
      });
  }
  for (let x = 0; x < characters.length; x++) {
      request(characters[x], async function (error, response, body) {
        if (error !== null) {
        console.error('errorCharData:', error); // Print the error if one occurred
      }
      if (Number(response.statusCode) !== 200) {
        console.log('statusCodeCharData:', response && response.statusCode); // Print the response status code if not an OK
      }
      const charData = JSON.parse(body); // Parse string to dict
      const charName = charData.name; // Get just the character name
      const result = await resolveAfter2Seconds();
      console.log(charName);
      });
  }
});
