/*
2021.08.22. 2021 Baekjoon algorithm problem #4195
친구 네트워크
*/

/*
<풀이 아이디어>
1) 
*/

const fs = require("fs");
const filePath = process.env.USER === "narastro" ? "./input.txt" : "/dev/stdin";
const input = fs.readFileSync(filePath).toString().split(`\n`);

function solution(input) {

    const node
    const findParents = ()=>{}

  const tests = Number(input.shift());
  let f;
  input.forEach((v,t)=>{
      if (Number(v)!==NaN){
        f = Number(v)
      }
      else{

      }
  })
}

console.log(solution(input));
