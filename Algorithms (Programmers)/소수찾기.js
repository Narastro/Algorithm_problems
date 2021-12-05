const isPrimeNumber = (num) => {
  if (num <= 2) return true;
  for (let i = 2; i < Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

const Permutations = (arr, selectNumber) => {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = Permutations(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
};

function solution(numbers) {
  let answer = 0;
  const stringNumbers = new Set();
  for (let i = 1; i <= numbers.length; i++) {
    stringNumbers.add(Permutations(numbers.split(""), i).join(""));
  }
  for (let numStr of stringNumbers) {
    if (isPrimeNumber(Number(numStr))) {
      console.log(numStr);
      answer += 1;
    }
  }
  return answer;
}
