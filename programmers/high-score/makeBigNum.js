/* 2021.06.27. 2021 Programmers High score kit
 * 큰 수 만들기
 */

function solution(number, k) {
  let answer = "";

  const cntMap = new Map();
  number.split("").forEach((num) => {
    cntMap.set(num, cntMap.get(num) ? cntMap.get(num) + 1 : 1);
  });
  let i = 0;
  while (true) {
    if (k === 0) {
      break;
    }
    if (cntMap.get(i.toString()) > 0) {
      cntMap.set(i.toString(), cntMap.get(i.toString()) - 1);
      k -= 1;
    } else {
      i += 1;
    }
  }

  i = 9;
  while (true) {
    if (i === -1) {
      break;
    }
    if (cntMap.get(i.toString()) > 0) {
      cntMap.set(i.toString(), cntMap.get(i.toString()) - 1);
      answer += i.toString();
    } else {
      i -= 1;
    }
  }
  return answer;
}

console.log(solution("1231234", 3));
