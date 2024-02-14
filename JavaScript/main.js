import { Octokit } from "octokit";
import dotenv from "dotenv";

dotenv.config();

const octokit = new Octokit({
    auth: `${process.env.TOKEN}`
});

// Get public repos
// var response = await octokit.request(`GET /users/${process.env.USERNAME}/repos`);
// var data = response.data;

// for(let i = 0; i < data.length; i++){
//     console.log(`Name: ${data[i].name} | Visibility: ${data[i].visibility}`)
// }

// Get private repos
var response = await octokit.request(`GET /search/repositories?q=user:${process.env.USERNAME}`)
var data = response.data;

// console.log(response.status)

// Get the JSON keys
// console.log(Object.keys(data))

for(let i = 0; i < data["items"].length; i++){
    console.log(`Name: ${data["items"][i].name} | Visibility: ${data["items"][i].visibility}`)
}