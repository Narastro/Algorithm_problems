/* 2022.4.4. 2021 Dev-Matching: 웹 백엔드
 * 로또의 최고 순위와 최저 순위;
 */

function solution(lottos, win_nums) {
  const answer = [7, 7];
  lottos.forEach((num) => {
    if (win_nums.includes(num)) {
      answer[0] -= 1;
      answer[1] -= 1;
    } else if (num === 0) {
      answer[0] -= 1;
    }
  });
  if (answer[0] === 7) answer[0] = 6;
  if (answer[1] === 7) answer[1] = 6;
  return answer;
}
