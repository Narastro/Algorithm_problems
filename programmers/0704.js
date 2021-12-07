// function solution(k, rates) {
//   let money = k;
//   let buy = false;
//   if (k < Math.min.apply(null, rates)) {
//     return k;
//   }
//   for (let i = 0; i < rates.length - 1; i++) {
//     if (!buy && rates[i] <= money && rates[i] < rates[i + 1]) {
//       money -= rates[i];
//       buy = true;
//       continue;
//     }
//     if (buy && rates[i + 1] < rates[i]) {
//       money += rates[i];
//       buy = false;
//       continue;
//     }
//   }
//   if (buy) {
//     money += rates[rates.length - 1];
//   }
//   return money;
// }

// console.log(solution(1, [3, 4, 5, 6, 2, 3, 4, 1, 2, 3, 1, 2]));

// function solution(money, cost) {
//   let maxLen = 0;
//   let left = 0;
//   let right = 0;
//   let subCost;
//   while (left !== cost.length) {
//     subCost = cost.slice(left, right + 1).reduce((a, b) => a + b, 0);
//     if (subCost <= money) {
//       maxLen = Math.max(maxLen, right - left + 1);
//       if (right !== cost.length - 1) {
//         right += 1;
//         continue;
//       } else {
//         break;
//       }
//     }
//     if (subCost > money) {
//       if (left !== right) {
//         left += 1;
//         continue;
//       } else if (right !== cost.length - 1) {
//         right += 1;
//         continue;
//       } else {
//         break;
//       }
//     }
//   }
//   return maxLen;
// }

// console.log(solution(100, [245, 317, 151, 192]));

const findBlock = (N, i, j, num) => {
  const blocks = [];
  blocks.push([i, j]);
  if (num === 0 && j + 2 < N) {
    blocks.push([i, j + 1]);
    blocks.push([i, j + 2]);
  } else if (num === 1 && i + 2 < N) {
    blocks.push([i + 1, j]);
    blocks.push([i + 2, j]);
  } else if (num === 2 && i + 1 < N && j + 1 < N) {
    blocks.push([i, j + 1]);
    blocks.push([i + 1, j + 1]);
  } else if (num === 3 && j + 1 < N && i - 1 >= 0) {
    blocks.push([i, j + 1]);
    blocks.push([i - 1, j + 1]);
  } else if (num === 4 && i + 1 < N && j + 1 < N) {
    blocks.push([i + 1, j]);
    blocks.push([i + 1, j + 1]);
  } else if (num === 5 && i + 1 < N && j + 1 < N) {
    blocks.push([i, j + 1]);
    blocks.push([i + 1, j]);
  } else {
    return false;
  }
  return blocks;
};

function solution(block, board) {
  let answer = 0;
  let N = board.length;

  const makeNewBoard = () => {
    let newBoard = new Array(N);
    for (let j = 0; j < N; j++) {
      newBoard[j] = new Array(N).fill(0);
      for (let i = 0; i < N; i++) {
        if (board[j][i] === 1) {
          newBoard[j][i] = 1;
        }
      }
    }
    return newBoard;
  };

  const findFullLine = (nBoard) => {
    let lines = 0;
    for (let j = 0; j < N; j++) {
      if (nBoard[j].reduce((a, b) => a + b) === N) {
        lines += 1;
      }
    }
    return lines;
  };

  for (let j = 0; j < N; j++) {
    for (let i = 0; i < N; i++) {
      if (board[j][i] === 0 && findBlock(N, i, j, block)) {
        const newBoard = makeNewBoard();
        for (let [x, y] of findBlock(N, i, j, block)) {
          newBoard[y][x] = 1;
        }
        answer = Math.max(answer, findFullLine(newBoard));
      }
    }
  }

  return answer;
}

console.log(
  solution(0, [
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
  ])
);
