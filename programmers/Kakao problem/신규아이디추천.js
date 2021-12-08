/* 2021.12.08. 2018 KAKAO Blind Recruitment
 * 신규 아이디 추천
 */

const step1 = (str) => str.toLowerCase();

const step2 = (str) => str.replace(/[^a-z\d-_.]/g, "");

const step3 = (str) => str.replace(/[.]+/g, ".");

const step4 = (str) => {
  if (str[0] === ".") str = str.slice(1);
  if (str.slice(-1) === ".") str = str.slice(0, -1);
  return str;
};

const step5 = (str) => {
  if (str.length === 0) return "a";
  else return str;
};

const step6 = (str) => {
  if (str.length >= 16) str = str.slice(0, 15);
  if (str.slice(-1) === ".") str = str.slice(0, -1);
  return str;
};

const step7 = (str) => {
  if (str.length <= 2) {
    const lastWord = str.slice(-1);
    str += lastWord + lastWord;
    str = str.slice(0, 3);
  }
  return str;
};

const solution = (new_id) =>
  step7(step6(step5(step4(step3(step2(step1(new_id)))))));

console.log("as" + "as");
