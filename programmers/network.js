/* 2021.06.27. 2021 Programmers High score kit
 * 네트워크
 */

function solution(n, computers) {
  let answer = 0;
  let visit = [];
  for (let i = 0; i < n; i++) {
    visit.push(false);
  }

  const dfs = (node) => {
    if (visit[node]) {
      return;
    }
    visit[node] = true;
    for (let j = 0; j < n; j++) {
      if (node !== j) {
        if (computers[node][j] === 1) {
          dfs(j);
        }
      }
    }
  };

  for (let w = 0; w < n; w++) {
    if (!visit[w]) {
      dfs(w);
      answer += 1;
    }
  }
  return answer;
}

console.log(
  solution(3, [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1],
  ])
);
