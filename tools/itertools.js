function Combinations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1); // 현재 문자 이후 배열을 자름
    const combinations = Combinations(rest, selectNumber - 1); // 그 배열에 대해 재귀으로 조합을 구함
    const attached = combinations.map((combination) => [fixed, ...combination]); // 그 조합에 현재 문자를 추가함
    results.push(...attached);
  });

  return results;
}

function Permutations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)]; // 조합과의 차이점은 현재 문자를 제외한 모든 배열을 자름
    const permutations = Permutations(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
}

exports.Combinations = Combinations;
exports.Permutations = Permutations;
