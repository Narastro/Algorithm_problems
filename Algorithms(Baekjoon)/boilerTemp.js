const fs = require("fs");
const filePath = process.env.USER === "narastro" ? "./input.txt" : "/dev/stdin";
const input = fs.readFileSync(filePath).toString().split(`\n`);

function solution(input) {}

console.log(solution(input));
