/* 2021.12.16. 프로그래머스 고득점 Kit - 깊이/너비 우선 탐색
 * 단어 변환
 */

const wordSlice = (word, index) => word.slice(0, index) + word.slice(index + 1);

const transWord = (word, path, words) => {
  const n = word.length;
  const possibleWords = [];
  for (let i = 0; i < n; i++) {
    const subWord = wordSlice(word, i);
    for (let w of words) {
      if (!path.includes(w) && wordSlice(w, i) === subWord)
        possibleWords.push(w);
    }
  }
  return possibleWords;
};

const solution = (begin, target, words) => {
  let answer = Infinity;
  const stack = [];
  stack.push({ word: begin, path: [begin] });
  while (stack.length !== 0) {
    const v = stack.pop();
    if (v.word === target) answer = Math.min(answer, v.path.length - 1);
    const possibleWords = transWord(v.word, v.path, words);
    for (let word of possibleWords) {
      stack.push({ word, path: [...v.path, word] });
    }
  }
  if (answer === Infinity) return 0;
  return answer;
};

console.log(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]));
