function solution(id_list, report, k) {
  const cntMap = new Map();
  const reportMap = new Map();
  const answer = new Map();
  [...new Set(report)].forEach((str) => {
    const reportArr = str.split(" ");
    const from = reportArr[0];
    const to = reportArr[1];
    cntMap.set(to, cntMap.has(to) ? cntMap.get(to) + 1 : 1);
    reportMap.set(
      to,
      reportMap.has(to) ? [...reportMap.get(to), from] : [from]
    );
  });
  for (let [key, value] of cntMap) {
    if (value >= k) {
      for (let k of reportMap.get(key)) {
        answer.set(k, answer.has(k) ? answer.get(k) + 1 : 1);
      }
    }
  }
  return id_list.map((id) => answer.get(id) || 0);
}
