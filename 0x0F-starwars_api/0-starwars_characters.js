#!/usr/bin/node

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

request(url + film, function (error, response, body) {
    console.error('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
//    console.log('body:', body); // Print the HTML for the SWAPI page.
    const payload = JSON.parse(body);
//    console.log (typeof payload);
    const characters = payload["characters"];
    let x = 0;
    for (x < characters.length) {
    	request(characters[x], function (error, response, body) {
	        console.error('errorCharData:', error); // Print the error if one occurred
	        console.log('statusCodeCharData:', response && response.statusCode); // Print the response status code if a response was received
	        let charData = JSON.parse(body);
	        let charName = charData['name'];
	        console.log(charName);
	        x = x + 1;
	    });
    };
});



