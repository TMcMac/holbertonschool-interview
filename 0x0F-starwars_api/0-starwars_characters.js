#!/usr/bin/node

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
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

const film = Number(args[2]);
const url = "https://swapi-api.hbtn.io/api/films/"
const request = require('request');

async function swapi() {
request(url + film, function (error, response, body) {
    if (error !== null) {
	console.error('error:', error); // Print the error if one occurred
    };
    if (Number(response.statusCode) !== 200) {
	console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    };
//    console.log('body:', body); // Print the HTML for the SWAPI page.
    const payload = JSON.parse(body);
//    console.log (typeof payload);
    const characters = payload["characters"];
    console.log(characters);
    for (let x = 0; x < characters.length; x++) {
	request(characters[x], function (error, response, body) {
	    await sleep(2000);
	    if (error !== null) {
	        console.error('errorCharData:', error); // Print the error if one occurred
	    };
	    if (Number(response.statusCode) !== 200) {
		console.log('statusCodeCharData:', response && response.statusCode); // Print the response status code if a response was received
	    };
	    console.log(characters[x]);
	    let charData = JSON.parse(body);
	    let charName = charData['name'];
	    console.log(charName);
	});
    };
});
};


