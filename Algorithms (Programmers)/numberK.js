/* 2021.04.28. 2021 Programmers High score kit
 * Kth number
 */

function solution(array, commands) {
    let answer = [];
    for (let [i,j,k] of commands) {
        let newArray = array.filter((value,fIndex)=>
        fIndex >= i-1 && fIndex < j)
        newArray.sort((a,b)=>a-b);
        answer.push(newArray[k-1])
    }
    return answer;
}
console.log(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]));