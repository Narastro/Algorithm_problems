class DefaultDict {
  constructor(type) {
    if (!type) throw Error("타입을 지정해주세요");
    if (type !== "int" && type !== "list") throw Error("타입을 확인해주세요");
    this.type = type;
    this.dict = new Map();
  }

  get(key) {
    if (!this.dict.has(key)) {
      if (this.type === "int") return 0;
      else return []; // 여기서 push를 하면 반영이 안됨을 주의하기!
    } else return this.dict.get(key);
  }

  set(key, value) {
    if (this.type === "int") {
      if (typeof value !== "number") throw Error("숫자만 입력 가능합니다.");
      this.dict.set(key, value);
    } else {
      const isExist = this.dict.has(key);
      this.dict.set(key, isExist ? [...this.dict.get(key), value] : [value]);
    }
  }
}

module.exports = DefaultDict;
