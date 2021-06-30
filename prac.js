// function solution(jobs) {
//   let time = 0;
//   let currentTime = 0;
//   let val = 0;

//   const n = jobs.length;
//   const Q = [];

//   // 0. 작업들을 들어온 순서대로 정렬
//   jobs.sort((a, b) => a[0] - b[0]);
//   // 0. 0초에 들어온 작업이 없는 경우, 가장 먼저 들어온 작업의 시간으로 이동
//   if (jobs[0][0] !== 0) {
//     currentTime = jobs[0][0];
//   }

//   while (true) {
//     // 4. Q에 아무것도 남지 않고 처리할 일도 없는 경우 종료
//     if (Q.length === 0 && jobs.length === 0) break;
//     // 1. 현재 시간보다 먼저 들어온 작업을 모두 Q에 삽입
//     while (jobs.length !== 0) {
//       if (jobs[0][0] <= currentTime) {
//         Q.push(jobs.shift());
//       } else {
//         break;
//       }
//     }
//     // 1-2. Q가 비어 있는 경우 가장 먼저 들어오는 데이터의 시간으로 이동
//     if (Q.length === 0) {
//       Q.push(jobs.shift());
//       currentTime = Q[0][0];
//       continue;
//     }
//     // 2. Q를 처리시간을 기준으로 오름차순 정렬
//     Q.sort((a, b) => a[1] - b[1]);
//     // 3. 데이터 처리
//     val = Q.shift();
//     currentTime += val[1];
//     time += currentTime - val[0];
//   }
//   return Math.floor(time / n);
// }

// console.log(
//   solution([
//     [24, 10],
//     [28, 39],
//     [43, 20],
//     [37, 5],
//     [47, 22],
//     [20, 47],
//     [15, 34],
//     [15, 2],
//     [35, 43],
//     [26, 1],
//   ])
// );

function solution(S) {
  let answer = "";
  const stringArr = S.split("");

  stringArr.sort();

  for (let alpha of stringArr) {
    if (
      stringArr.includes(alpha.toLowerCase()) &&
      stringArr.includes(alpha.toUpperCase())
    ) {
      answer = alpha.toUpperCase();
    }
  }

  return answer === "" ? "NO" : answer;
}

console.log(solution("AacdbB"));

// function solution(A) {
//   function proto(i) {
//     this.index = i;
//   }
//   proto.prototype.value = function () {
//     return A[this.index];
//   };
//   return A.map((v, i) => new proto(i));
// }
// T = solution([4, 2]);
// console.log(T[0].value === T[1].value);
