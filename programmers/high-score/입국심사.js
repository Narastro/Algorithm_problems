/* 2021.12.16. 프로그래머스 고득점 Kit - 이분탐색
 * 입국심사
 */

const solution = (n, times) => {
  times.sort((a, b) => a - b);
  let answer;
  let start = 1;
  let end = n * times[times.length - 1];
  let mid;
  let reqTime;

  while (start <= end) {
    mid = Math.floor((start + end) / 2);
    reqTime = times.reduce((a, b) => a + Math.floor(mid / b), 0);
    console.log(reqTime, start, end);
    if (reqTime >= n) {
      end = mid - 1;
      answer = mid;
    } else start = mid + 1;
  }
  return answer;
};
