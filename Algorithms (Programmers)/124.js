/* 2021.05.10. 2021 Programmers High score kit
 * 124 Country's Number
 */

// function solution(n) {
//     let answer = '';
//     let num = n+1;
//     const LOG3 = Math.log(3);
//     const N = Math.floor(Math.log(n)/LOG3);
//     for (let i=0;i<N+1;i++){
//         const EXP = N-i;
//         const tmp = Math.floor( num / Math.pow(3,EXP));
//         num = num % Math.pow(3,EXP)
//         if (tmp === 0){
//             answer += '1';
//         }else if (tmp === 1){
//             answer += '2'
//         }else{
//             answer += '4'
//         }
//     }
//     return answer;
// }
'use strict';
function solution(n){
    if (n<=3){
        return '124'[n-1];
    }else{
        const q = parseInt((n-1)/3);
        const r = (n-1) % 3;
        return solution(q)+'124'[r];
    }
}

console.log(solution(10))