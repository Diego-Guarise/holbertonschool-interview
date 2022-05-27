#!/usr/bin/node
// Star Wars Characters

const request = require('request');
const { argv } = require('process');
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];

request.get(url, function (error, response, body) {
    if (error) {
        console.log(error);
        return;
    }
    const json = JSON.parse(body);
    const array = json.characters;
    array.forEach(async function (person) {
        try {
        const result = await makeRequest(person);
        const dic = JSON.parse(result)
        console.log(dic.name);
        } catch (error) {
        console.error(error);
        }
    })
    });


    function makeRequest(path) {
        return new Promise(function (resolve, reject) {
            request.get(path, function (error, response, body) {
                if (error) {
                reject(error);
                }
                resolve(body)
            });
        });
    }