#!/usr/bin/node

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms)); // basic sleep function
};

const args = process.argv;

if (args.length != 3) {
    console.log("Usage: ./0-starwars_characters.js <Film Number>");
    process.exit(1);
};

if (Number.isInteger(Number(args[2])) == false) {
    console.log("Usage: ./0-starwars_characters.js <Film Number>");
    process.exit(1);
}

const film = Number(args[2]); // Film number in relase date order
const url = "https://swapi-api.hbtn.io/api/films/" // Swapi films base url
const request = require('request');

	request(url + film, function (error, response, body) {
		if (error !== null) {
		console.error('error:', error); // Print the error if one occurred
		};
		if (Number(response.statusCode) !== 200) {
		console.log('statusCode:', response && response.statusCode); // Print the response status code if not an OK
		};
		const payload = JSON.parse(body);
		const characters = payload["characters"]; // An array of character urls for the SWAPI
		console.log(characters); // Print the whole list, for testing
		for (let x = 0; x < characters.length; x++) {
			request(characters[x], function (error, response, body) {
				if (error !== null) {
					console.error('errorCharData:', error); // Print the error if one occurred
				};
				if (Number(response.statusCode) !== 200) {
				console.log('statusCodeCharData:', response && response.statusCode); // Print the response status code if not an OK
				};
				console.log(characters[x]); // The character specific URL
				let charData = JSON.parse(body); // Parse string to dict
				let charName = charData['name']; // Get just the character name
				console.log(charName);
			});
		};
	});

