/* 2021.12.13. 2018 KAKAO BLIND RECRUITMENT
 * 뉴스 클러스터링
 */

// 파이썬 defaultdict이 그립다..

const makeMultiSets = (str) =>
  str
    .toLowerCase()
    .split("")
    .map((char, index, origin) => {
      if (index !== origin.length - 1) return char + origin[index + 1];
    })
    .slice(0, -1)
    .filter((set) => !/[^a-zA-Z]/g.test(set));

const findWordCount = (multiSets) => {
  const cntMap = new Map();
  multiSets.forEach((str) => {
    cntMap.set(str, cntMap.has(str) ? cntMap.get(str) + 1 : 1);
  });
  return cntMap;
};

const findUionSet = (set1, set2) => {
  for (let [key, value] of set1) {
    set2.set(key, set2.has(key) ? Math.max(value, set2.get(key)) : value);
  }
  return set2;
};

const findDifferSet = (set1, set2) => {
  const differSet = new Map();
  for (let [key, value] of set1) {
    if (set2.has(key)) differSet.set(key, Math.min(value, set2.get(key)));
  }
  return differSet;
};

const solution = (str1, str2) => {
  const CONSTANT = 65536;
  const multiSet1 = makeMultiSets(str1);
  const multiSet2 = makeMultiSets(str2);
  const cntMap1 = findWordCount(multiSet1);
  const cntMap2 = findWordCount(multiSet2);
  const differSet = findDifferSet(cntMap1, cntMap2);
  const unionSet = findUionSet(cntMap1, cntMap2);
  if (differSet.size === 0 && unionSet.size === 0) return CONSTANT;
  if (differSet.size === 0) return 0;
  return Math.floor(
    ([...differSet.values()].reduce((a, b) => a + b) /
      [...unionSet.values()].reduce((a, b) => a + b)) *
      CONSTANT
  );
};

console.log(solution("aa1+aa2", "AAAA12"));
