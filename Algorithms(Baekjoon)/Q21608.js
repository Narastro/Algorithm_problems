const PriorityQueue = require("../PriorityQueue.js");
const itertools = require("../itertools");
const fs = require("fs");
const filePath = process.env.USER === "narastro" ? "./input.txt" : "/dev/stdin";
const input = fs.readFileSync(filePath).toString().split(`\n`);

function closeLikePeople() {}

function solution(input) {
  const N = Number(input[0]);
  const info = input.slice(1);
  const table = new Array(N);
  for (let i = 0; i < N; i++) {
    table[i] = [...new Array(N).fill(0)];
  }

  return table;
}

console.log(solution(input));
