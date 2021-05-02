// 2021.04.29. 2021 Programmers High score kit
// Test

function solution(answers) {
    let answer = [];
    let person_1 = [],
        person_2 = [],
        person_3 = [];
    person_1 = answers.filter((a,i) => a===(i%5+1))
    person_2 = answers.filter((a,i) => i%2===0? a===2 : Math.floor((i/2))
    person_3 = answers.filter((a,i) => )
    return person_1;
}

console.log(solution([1,2,3,4,5]))
