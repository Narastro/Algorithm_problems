/* 2021.06.27. 2021 Programmers High score kit
 * H index
 */

function solution(citations) {
  let answer = 0;
  citations.sort((a, b) => b - a);
  for (let i = 0; i < citations.length; i++) {
    if (citations[i] >= i + 1) {
      answer = i + 1;
    }
  }
  return answer;
}

console.log(solution([3, 0, 6, 1, 5]));
