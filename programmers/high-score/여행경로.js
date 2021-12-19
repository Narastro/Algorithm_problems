/* 2021.12.16. 프로그래머스 고득점 Kit - 깊이/너비 우선 탐색
 * 여행 경로
 */

const solution = (tickets) => {
  const answer = [];
  const dfs = (node, tks, path) => {
    const newPath = [...path, node];
    if (tks.length === 0) answer.push(newPath);
    else {
      tks.map((ticket, index) => {
        if (ticket[0] === node) {
          const [[from, to]] = [...tks].splice(index, 1);
          dfs(to, [...tks], newPath);
        }
      });
    }
  };
  dfs("ICN", tickets, []);
  return answer.sort()[0];
};

console.log(
  solution([
    ["ICN", "SFO"],
    ["ICN", "ATL"],
    ["SFO", "ATL"],
    ["ATL", "ICN"],
    ["ATL", "SFO"],
  ])
);
