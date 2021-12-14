/* 2021.12.14. 2020 카카오 인턴십
 * 수식 최대화
 */

function Permutations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    const permutations = Permutations(rest, selectNumber - 1);
    const attached = permutations.map((permutation) => [fixed, ...permutation]);
    results.push(...attached);
  });

  return results;
}

const findIndex = (arr, target) =>
  arr
    .map((str, index) => {
      if (str === target) return index;
      else return -1;
    })
    .filter((num) => num !== -1);

const calculOper = (opers, sign, nums) => {
  let newSign = sign;
  let newNums = nums;
  opers.forEach((targetOper) => {
    const signArr = [];
    const numsArr = [];
    newSign.forEach((op, index) => {
      if (op === targetOper) {
        if (index > 0 && newSign[index - 1] === targetOper) {
          numsArr.push(eval(numsArr.pop() + op + newNums[index + 1]));
        } else {
          numsArr.push(eval(newNums[index] + op + newNums[index + 1]));
        }
      } else if (index > 0 && newSign[index - 1] === targetOper) {
        signArr.push(op);
      } else {
        numsArr.push(newNums[index]);
        signArr.push(newSign[index]);
      }
      if (index === newSign.length - 1 && op !== targetOper)
        numsArr.push(newNums[index + 1]);
    });
    newSign = signArr;
    newNums = numsArr;
  });
  return Math.abs(newNums[0]);
};

const solution = (expression) => {
  const nums = expression.split(/[^0-9]/g);
  const signs = expression.match(/[^0-9]/g);
  const signType = [...new Set(signs)];
  const operArr = Permutations(signType, signType.length);
  let maxVal = 0;
  operArr.forEach((opers) => {
    maxVal = Math.max(maxVal, calculOper(opers, signs, nums));
  });
  return maxVal;
};

console.log(solution("50*6-3*2"));
