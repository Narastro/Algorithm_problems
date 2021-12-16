/* 2021.12.16. 프로그래머스 고득점 Kit - 깊이/너비 우선 탐색
 * 타겟 넘버
 */

function solution(numbers, target) {
  let answer = 0;
  const dfs = (depth, sum) => {
    if (depth === numbers.length) {
      if (sum === target) answer += 1;
      return;
    }
    dfs(depth + 1, sum + numbers[depth]);
    dfs(depth + 1, sum - numbers[depth]);
  };
  dfs(0, 0);
  return answer;
}

console.log(solution([1, 2, 3, 4, 5], 5));
