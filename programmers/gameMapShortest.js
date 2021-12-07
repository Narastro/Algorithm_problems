/* 2021.06.30. 2021 Programmers High score kit
 * 게임 맵 최단거리
 */

/*
2차원 배열의 BFS 기본 문제지만,
자바스크립트로 구현함에 어려움을 겪었다.
배웠던 점은 다음과 같다.
1. 2차원 배열을 생성하는 법 (new Array(N).fill(new Array()) 이 방식은 안된다 주의할 것.)
2. 좌표를 큐에 넣을 때 object로 넣는 것
3. const {x,y} = Q.shift() 즉 const x,y = Q.shift().x, Q.shift().y를 한 번에!
*/

function solution(maps) {
  const M = maps[0].length;
  const N = maps.length;

  const bfs = () => {
    const Q = [];
    const visit = new Array(N);
    for (let j = 0; j < N; j++) {
      visit[j] = new Array(M).fill(0);
    }

    const dx = [1, -1, 0, 0];
    const dy = [0, 0, 1, -1];

    Q.push({ x: 0, y: 0 });
    visit[0][0] = 1;

    while (Q.length !== 0) {
      const { x, y } = Q.shift();
      const d = visit[y][x];

      if (x === M - 1 && y === N - 1) {
        return d;
      }

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i];
        const ny = y + dy[i];
        if (
          0 <= nx &&
          nx < M &&
          0 <= ny &&
          ny < N &&
          visit[ny][nx] === 0 &&
          maps[ny][nx] !== 0
        ) {
          Q.push({ x: nx, y: ny });
          visit[ny][nx] = d + 1;
        }
      }
    }
    return -1;
  };

  return bfs();
}

console.log(
  solution([
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1],
  ])
);
