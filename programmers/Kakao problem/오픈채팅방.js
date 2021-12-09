/* 2021.12.09. 2019 KAKAO Blind Recruitment
 * 오픈 채팅방
 */

const solution = (records) => {
  const nicknameMap = new Map();
  const recordArr = [];
  for (let record of records) {
    const strArr = record.split(" ");
    const action = strArr[0];
    const uid = strArr[1];
    if (action !== "Leave") {
      const nickname = strArr[2];
      nicknameMap.set(uid, nickname);
    }
    if (action !== "Change") recordArr.push({ action, uid });
  }
  return recordArr.map((obj) => {
    const nickname = nicknameMap.get(obj.uid);
    return obj.action === "Enter"
      ? `${nickname}님이 들어왔습니다.`
      : `${nickname}님이 나갔습니다.`;
  });
};
