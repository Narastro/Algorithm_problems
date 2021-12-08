/* 2021.12.08. 2021 KAKAO 인턴십
 * 숫자 문자열과 영단어
 */

const solution = (s) =>
  Number(
    s
      .replace(/zero/g, "0")
      .replace(/one/g, "1")
      .replace(/two/g, "2")
      .replace(/three/g, "3")
      .replace(/four/g, "4")
      .replace(/five/g, "5")
      .replace(/six/g, "6")
      .replace(/seven/g, "7")
      .replace(/eight/g, "8")
      .replace(/nine/g, "9")
  );
