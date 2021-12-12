/* 2021.12.10. 2018 KAKAO BLIND RECRUITMENT
 * 추석 트래픽
 */

const timeToMillisec = (str) => {
  const strArr = str.split(":");
  const hours = Number(strArr[0]);
  const minutes = Number(strArr[1]);
  const milliseconds = Number(strArr[2]) * 1000;
  const total = milliseconds + minutes * 60 * 1000 + hours * 60 * 60 * 1000;
  return total;
};

const findStartTime = (endTime, time) =>
  endTime - (Number(time.split("s")[0]) * 1000 - 1);

const compareTimeInRange = (time, log, duration) =>
  log <= time && time < log + duration;

const compareTimeOutRange = (start, end, log, duration) =>
  log >= start && log + duration <= end;

const solution = (lines) => {
  const logs = [];
  const timeInfo = [];
  let maxCount = 0;

  lines.forEach((line) => {
    const endTime = timeToMillisec(line.split(" ")[1]);
    const startTime = findStartTime(endTime, line.split(" ")[2]);
    timeInfo.push({ startTime, endTime });
    logs.push(startTime, endTime);
  });

  logs.sort();
  logs.forEach((log) => {
    const DURATION = 1000;
    const count = timeInfo.filter(
      ({ startTime, endTime }) =>
        compareTimeInRange(startTime, log, DURATION) ||
        compareTimeInRange(endTime, log, DURATION) ||
        compareTimeOutRange(startTime, endTime, log, DURATION)
    ).length;
    maxCount = Math.max(maxCount, count);
  });
  return maxCount;
};
