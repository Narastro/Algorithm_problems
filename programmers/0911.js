//1번

// function solution(id_list, report, k) {
//   const answer = new Array(id_list.length).fill(0);
//   const infoObj = {};
//   const nameToIndex = new Map();
//   const reportSet = new Set(report);

//   id_list.forEach((id, index) => {
//     infoObj[id] = { num: 0, from: [] };
//     nameToIndex.set(id, index);
//   });

//   reportSet.forEach((rep) => {
//     const from = rep.split(" ")[0];
//     const to = rep.split(" ")[1];
//     infoObj[to].num += 1;
//     infoObj[to].from.push(from);
//   });

//   id_list.forEach((id) => {
//     if (infoObj[id].num >= k) {
//       infoObj[id].from.forEach((name) => {
//         const index = nameToIndex.get(name);
//         answer[index] += 1;
//       });
//     }
//   });
//   return answer;
// }

// console.log(
//   solution(
//     ["muzi", "frodo", "apeach", "neo"],
//     ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
//     2
//   )
// );

//2번
// const isPrimeNum = (num) => {
//   if (num <= 1) return false;
//   if (num === 2) return true;
//   for (let i = 2; i <= Math.sqrt(num); i++) {
//     if (num % i === 0) return false;
//   }
//   return true;
// };

// function solution(n, k) {
//   let answer = 0;
//   const num = n.toString(k);
//   const splitNum = num.split("0");

//   for (let n of splitNum) {
//     if (isPrimeNum(Number(n))) {
//       answer += 1;
//     }
//   }
//   return answer;
// }

// console.log(solution(110011, 10));

//3번

// const convertTime = (timeStr) => {
//   const hours = timeStr.split(":")[0];
//   const minutes = timeStr.split(":")[1];
//   return Number(hours) * 60 + Number(minutes);
// };

// const makeCarInfos = (carRecord, records) => {
//   records.forEach((record) => {
//     const timeStr = record.split(" ")[0];
//     const time = convertTime(timeStr);
//     const carNum = record.split(" ")[1];
//     const isIn = record.split(" ")[2] === "IN";

//     carRecord[carNum] ? null : (carRecord[carNum] = { totalTime: 0 });

//     if (isIn) {
//       carRecord[carNum].lastTime = time;
//       carRecord[carNum].isIn = isIn;
//     } else {
//       carRecord[carNum].totalTime += time - carRecord[carNum].lastTime;
//       carRecord[carNum].isIn = isIn;
//     }
//   });

//   Object.keys(carRecord).forEach((num) => {
//     if (carRecord[num].isIn) {
//       carRecord[num].totalTime +=
//         convertTime("23:59") - carRecord[num].lastTime;
//       carRecord[num].isIn = false;
//     }
//   });

//   return carRecord;
// };

// const calculFee = (carInfos, fees) => {
//   const carFees = [];
//   const basicTime = fees[0];
//   const unitTime = fees[2];
//   const basicFee = fees[1];
//   const unitFee = fees[3];

//   for (let carNum in carInfos) {
//     const feeObj = { carNum };
//     if (carInfos[carNum].totalTime >= basicTime) {
//       carInfos[carNum].totalTime -= basicTime;
//       feeObj.fee = basicFee;
//       feeObj.fee += Math.ceil(carInfos[carNum].totalTime / unitTime) * unitFee;
//     } else {
//       feeObj.fee = basicFee;
//     }
//     carFees.push(feeObj);
//   }
//   return carFees
//     .sort((a, b) => Number(a.carNum) - Number(b.carNum))
//     .map((obj) => obj.fee);
// };

// function solution(fees, records) {
//   const carInfos = makeCarInfos({}, records);
//   const carFees = calculFee(carInfos, fees);
//   return carFees;
// }

// console.log(
//   solution(
//     [180, 5000, 10, 600],
//     [
//       "05:34 5961 IN",
//       "06:00 0000 IN",
//       "06:34 0000 OUT",
//       "07:59 5961 OUT",
//       "07:59 0148 IN",
//       "18:59 0000 IN",
//       "19:09 0148 OUT",
//       "22:59 5961 IN",
//       "23:00 5961 OUT",
//     ],
//     [14600, 34400, 5000]
//   )
// );

//4번

const calculWinScore = (info, k) => {};

function solution(n, info) {
  const answer = [];
  let k = 1;

  if (info[0] === n) return [-1];

  calculWinScore(info, k);

  return answer;
}

//5번

// const createTree = (info, edges) => {
//   const tree = {};
//   info.forEach((v, i) => {
//     tree[i] = { isWolf: v === 1, next: [] };
//   });
//   for (let [from, to] of edges) {
//     tree[from].next.push(to);
//   }
//   return tree;
// };

// const findSheep = (tree, start) => {
//   const Q = [start];
//   const nextNodes = [];
//   let curSheep = 1;
//   let curWolf = 0;

//   while (Q.length !== 0) {
//     const v = Q.pop();

//     if (tree[v].isWolf) curWolf += 1;

//     if (curSheep === curWolf) return curSheep;

//     for (let num of tree[v].next) {
//       if (!tree[num].isWolf) {
//         Q.unshift(String(num));
//         curSheep += 1;
//       } else {
//         Q.push(String(num));
//       }
//     }
//   }
// };

// function solution(info, edges) {
//   let answer = 0;
//   const tree = createTree(info, edges);
//   console.log(tree);
//   const curSheep = findSheep(tree, "0", 0);
//   console.log(curSheep);

//   return answer;
// }

// console.log(
//   solution(
//     [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
//     [
//       [0, 1],
//       [0, 2],
//       [1, 3],
//       [1, 4],
//       [2, 5],
//       [2, 6],
//       [3, 7],
//       [4, 8],
//       [6, 9],
//       [9, 10],
//     ]
//   )
// );
