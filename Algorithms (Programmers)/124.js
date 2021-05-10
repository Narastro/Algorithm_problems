/* 2021.05.10. 2021 Programmers High score kit
 * 124 Country's Number
 */

function solution(n) {
    let answer = '';
    let num = n+1;
    const LOG3 = Math.log(3);
    const N = Math.floor(Math.log(n)/LOG3);
    for (let i=0;i<N+1;i++){
        const EXP = N-i;
        const tmp = Math.floor( num / Math.pow(3,EXP));
        num = num % Math.pow(3,EXP)
        if (tmp === 0){
            answer += '1';
        }else if (tmp === 1){
            answer += '2'
        }else{
            answer += '4'
        }
    }
    return answer;
}

console.log(solution(10))