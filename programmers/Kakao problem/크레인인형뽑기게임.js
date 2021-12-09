/* 2021.12.09. 2019 KAKAO 겨울 인턴십
 * 크레인 인형뽑기 게임
 */

const getDepth = (board, num) => {
  let depth = 0;
  while (depth < board.length && board[depth][num] === 0) {
    if (depth === board.length - 1) return depth;
    depth += 1;
  }
  return depth;
};

const solution = (board, moves) => {
  const basket = [];
  let answer = 0;
  moves.forEach((position) => {
    position -= 1;
    const index = getDepth(board, position);
    const pick = board[index][position];
    if (!pick) return;
    else if (basket.length !== 0 && basket.slice(-1)[0] === pick) {
      answer += 2;
      basket.pop();
    } else {
      basket.push(pick);
    }
    board[index][position] = 0;
  });
  return answer;
};

console.log(
  solution(
    [
      [0, 0, 0, 0, 0],
      [0, 0, 1, 0, 3],
      [0, 2, 5, 0, 1],
      [4, 2, 4, 4, 2],
      [3, 5, 1, 3, 1],
    ],
    [1, 5, 3, 5, 1, 2, 1, 4]
  )
);
