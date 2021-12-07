/* 2021.06.30. 2021 Programmers High score kit
 * 튜플
 */

/*
자바스크립트의 forEach와 map 연습하기 좋은 문제
*/

function solution(s) {
  const answer = [];
  const ansSet = new Set();
  s.slice(2, s.length - 2)
    .split("},{")
    .sort((a, b) => a.length - b.length)
    .forEach((s) => s.split(",").forEach((v) => ansSet.add(Number(v))));

  ansSet.forEach((v) => answer.push(v));
  return answer;
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"));
