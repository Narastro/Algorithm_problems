/* 2021.12.14. 2021 KAKAO BLIND RECRUITMENT
 * 순위 검색
 */

const binarySearch = (arr, target) => {
  if (!arr) return 0;
  arr.sort((a, b) => a - b);
  let start = 0;
  let end = arr.length - 1;
  while (start < end) {
    let mid = Math.floor((end + start) / 2);
    if (arr[mid] >= target) end = mid;
    else start = mid + 1;
  }
  return arr.length - start;
};

function Combinations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = Combinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
}

const solution = (infos, querys) => {
  const table = new Map();
  const totalTable = [];

  infos.forEach((info) => {
    const arr = info.split(" ");
    const score = Number(arr.pop());
    totalTable.push(score);

    for (let k = 1; k <= 4; k++) {
      Combinations(arr, k).forEach((combs) => {
        const str = combs.join("");
        table.set(str, table.has(str) ? [...table.get(str), score] : [score]);
      });
    }
  });

  return querys.map((line) => {
    const arr = line.split(" ");
    const score = Number(arr.pop());
    const query = arr.join("").replace(/and|-/g, "");
    if (!query) return binarySearch(totalTable, score);
    return binarySearch(table.get(query), score);
  });
};

console.log(
  solution(
    [
      "java backend junior pizza 150",
      "python frontend senior chicken 210",
      "python frontend senior chicken 150",
      "cpp backend senior pizza 260",
      "java backend junior chicken 80",
      "python backend senior chicken 50",
    ],
    [
      "java and backend and junior and pizza 100",
      "python and frontend and senior and chicken 200",
      "cpp and - and senior and pizza 250",
      "- and backend and senior and - 150",
      "- and - and - and chicken 100",
      "- and - and - and - 150",
    ]
  )
);
