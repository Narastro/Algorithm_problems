/* 2021.12.13. 2021 KAKAO BLIND RECRUITMENT
 * 메뉴 리뉴얼
 */

// 이렇게 고차함수를 많이 썼는데도 시간은 그리 오래 걸리지 않네...
// 풀이가 마음에 들지 않는다...ㅠ

function Combinations(arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((value) => [value]);

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = Combinations(rest, selectNumber - 1);
    const attached = combinations.map((combination) => [fixed, ...combination]);
    results.push(...attached);
  });

  return results;
}

const solution = (orders, course) => {
  const counter = new Map();
  const maxCounter = new Map();
  orders.forEach((order) =>
    course
      .map((num) => Combinations(order.split(""), num))
      .forEach((arr) =>
        arr
          .map((strArr) => strArr.sort().join(""))
          .forEach((menu) =>
            counter.set(menu, counter.has(menu) ? counter.get(menu) + 1 : 1)
          )
      )
  );

  return [...counter.entries()]
    .filter((item) => item[1] > 1)
    .sort((a, b) => b[0].length - a[0].length)
    .map((item) => {
      const n = item[0].length;
      maxCounter.set(
        n,
        maxCounter.has(n) ? Math.max(item[1], maxCounter.get(n)) : item[1]
      );
      return item;
    })
    .filter((item) => item[1] === maxCounter.get(item[0].length))
    .map((item) => item[0])
    .sort();
};
