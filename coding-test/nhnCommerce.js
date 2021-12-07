// let preVal = logs[0];
// let cnt = 0;
// const answer = [];
// logs.forEach((log) => {
//   if (preVal === log) {
//     cnt += 1;
//   } else {
//     answer.push(preVal + (cnt <= 1 ? "" : ` (${cnt})`));
//     cnt = 1;
//     preVal = log;
//   }
// });
// answer.push(preVal + (cnt <= 1 ? "" : ` (${cnt})`));

// console.log(answer.length);
// console.log(answer.join(`\n`));

//1111111111111111111111

// const lines = [];
// rl.on("line", function (line) {
//   lines.push(line);
// }).on("close", function () {
//   let T = lines.shift();
//   while (T-- !== 0) {
//     const info = lines.shift().split(" ");
//     let N = Number(info[0]);
//     let M = Number(info[1]);
//     let cnt = 0;
//     let check = 1;
//     const applyList = lines.shift().split(" ");

//     const phoneNum = new Map();
//     while (M !== 0 && N !== 0) {
//       N -= 1;
//       cnt += 1;
//       const applyPhone = applyList.shift();
//       if (!phoneNum.has(applyPhone)) {
//         phoneNum.set(applyPhone, true);
//         M -= 1;
//         check = cnt;
//       }
//     }
//     if (N === 0 && check !== cnt) {
//       console.log(check);
//     } else {
//       console.log(cnt);
//     }
//   }
//   process.exit();
// });

//2222222222222222222222222222

// const readline = require("readline");

// function Combinations(arr, selectNumber) {
//   const results = [];
//   if (selectNumber === 1) return arr.map((value) => [value]);

//   arr.forEach((fixed, index, origin) => {
//     const rest = origin.slice(index + 1);
//     const combinations = Combinations(rest, selectNumber - 1);
//     const attached = combinations.map((combination) => [fixed, ...combination]);
//     results.push(...attached);
//   });

//   return results;
// }

// function findMax(arr, table, N) {
//   let maxVal = 0;
//   for (let i = 0; i < arr.length; i++) {
//     let subSum = 0;
//     for (let j = 0; j < N; j++) {
//       const pick = arr[i][j];
//       subSum += Number(table[j][pick]);
//     }
//     maxVal = Math.max(maxVal, subSum);
//   }
//   return maxVal;
// }

// (async () => {
//   let rl = readline.createInterface({ input: process.stdin });

//   const lines = [];

//   for await (const line of rl) {
//     lines.push(line);
//     rl.close();
//   }
//   const info = lines.shift().split(" ");
//   const N = Number(info[0]);
//   const M = Number(info[1]);
//   const K = Number(info[2]);
//   const totalNum = new Array(K - 1).fill(0).map((v, i) => i + 1);
//   const findNums = Combinations(totalNum, N - 1);
//   const findIndex = findNums.map((arr) => {
//     const index = [];
//     let pre = 0;
//     while (arr.length !== 0) {
//       const thisVal = arr.shift();
//       index.push(thisVal - pre - 1);
//       pre = thisVal;
//     }
//     index.push(K - pre - 1);
//     return index;
//   });
//   const table = lines.map((val) => val.slice(0, -1).split(" ").reverse());

//   console.log(findMax(findIndex, table, N));

//   process.exit();
// })();

//333333333333333333

const findTime = (toMap, fromMap, planet, x) => {};

const bfs = (toMap, start, end) => {
  const Q = [];
  const visit = new Map();
  Q.push({ node: start, time: 0 });
  while (Q.length !== 0) {
    const v = Q.shift();
    if (v.node === end) {
      return v.time;
    }

    for (let nextNode of toMap.get(v.node)) {
      if (!visit.has(nextNode)) {
        visit.set(nextNode, 1);
        Q.push({ node: nextNode, time: 1 });
      }
    }
  }
};

(async () => {
  let rl = readline.createInterface({ input: process.stdin });

  const lines = [];

  for await (const line of rl) {
    lines.push(line);
    rl.close();
  }

  const info = lines.shift().split(" ");
  const N = Number(info[0]);
  const M = Number(info[1]);
  const G = Number(info[2]);
  const toMap = new Map();
  const fromMap = new Map();

  for (let i = 0; i < M - 1; i++) {
    const value = lines.shift().split(" ");
    const from = value[0];
    const to = value[1];
    toMap.set(from, toMap.has(from) ? [...toMap.get(from), to] : [to]);
    fromMap.set(to, fromMap.has(to) ? [...fromMap.get(to), from] : [from]);
  }

  const lastLine = lines.pop().split(" ");
  const x = lastLine[0];
  const start = lastLine[1];
  const end = lastLine[2];

  process.exit();
})();
