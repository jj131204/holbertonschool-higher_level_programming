#!/usr/bin/node
//  reads and prints the content of a file

const argv = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + argv;

const request = require('request');

request(url, function (err, result, body) {
  console.log(JSON.parse(body).title);
  if (err) {
    console.log(err);
  }
});
