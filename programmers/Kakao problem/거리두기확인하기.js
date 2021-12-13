/* 2021.12.13. 2021 카카오 채용연계형 인턴십
 * 거리두기 확인하기
 */

class NodeQueue {
  constructor(value) {
    this.next = null;
    this.value = value;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  push(value) {
    const nodeQueue = new NodeQueue(value);
    if (!this.size) this.head = nodeQueue;
    else this.tail.next = nodeQueue;
    this.tail = nodeQueue;
    this.size++;
  }

  popleft() {
    if (!this.size) return null;
    const value = this.head.value;
    this.head = this.head.next;
    this.size--;
    if (!this.size) this.tail = null;
    return value;
  }

  isEmpty() {
    return this.size === 0;
  }
}

const solution = (places) => {
  const N = 5;
  const dx = [0, 1, -1, 0];
  const dy = [1, 0, 0, -1];

  const isSafe = (place, row, col) => {
    const visit = new Array(N);
    for (let i = 0; i < N; i++) {
      visit[i] = new Array(N).fill(-1);
    }
    const queue = new Queue();
    queue.push({ row, col });
    visit[row][col] = 0;
    while (!queue.isEmpty()) {
      const node = queue.popleft();
      const dist = visit[node.row][node.col];
      for (let i = 0; i < 4; i++) {
        const nRow = node.row + dy[i];
        const nCol = node.col + dx[i];
        const newNode = { row: nRow, col: nCol };
        if (
          0 < nRow &&
          0 < nCol &&
          nRow < N &&
          nCol < N &&
          visit[nRow][nCol] === -1 &&
          place[nRow][nCol] !== "X"
        ) {
          if (dist < 2 && place[nRow][nCol] === "P") {
            return false;
          }
          queue.push(newNode);
          visit[nRow][nCol] = dist + 1;
        }
      }
    }
    return true;
  };

  return places.map((place) => {
    let answer = true;
    place.forEach((line, row) => {
      line.split("").forEach((value, col) => {
        if (value === "P" && !isSafe(place, row, col)) answer = false;
      });
    });
    if (answer) return 1;
    else return 0;
  });
};

console.log(
  solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
  ])
);
