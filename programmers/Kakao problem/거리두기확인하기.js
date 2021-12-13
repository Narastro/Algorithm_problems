/* 2021.12.13. 2021 카카오 채용연계형 인턴십
 * 거리두기 확인하기
 */

const solution = (places) => {
  const N = 5;
  const dx = [0, 1, -1, 0];
  const dy = [1, 0, 0, -1];

  const isSafe = (value, place, row, col) => {
    if (value === "P") {
      for (let i = 0; i < 4; i++) {
        const nRow = row + dy[i];
        const nCol = col + dx[i];
        if (
          0 <= nRow &&
          0 <= nCol &&
          nRow < N &&
          nCol < N &&
          place[nRow][nCol] === "P"
        )
          return false;
      }
    } else if (value === "O") {
      let cnt = 0;
      for (let i = 0; i < 4; i++) {
        const nRow = row + dy[i];
        const nCol = col + dx[i];
        if (
          0 <= nRow &&
          0 <= nCol &&
          nRow < N &&
          nCol < N &&
          place[nRow][nCol] === "P"
        ) {
          cnt += 1;
          if (cnt > 1) return false;
        }
      }
    }
    return true;
  };

  return places.map((place) => {
    let answer = true;
    place.forEach((line, row) => {
      line.split("").forEach((value, col) => {
        if (value !== "X" && !isSafe(value, place, row, col)) answer = false;
      });
    });
    if (answer) return 1;
    else return 0;
  });
};

console.log(solution([["OP", "PX"]]));
