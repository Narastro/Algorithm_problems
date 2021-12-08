/* 2021.05.06. 2021 Programmers High score kit
 * Function Development
 */

function solution(progresses, speeds) {
    let answer = [];

    const days = progresses.map((v,i)=>{
        return Math.ceil((100-v)/speeds[i])
    })

    while(days.length !== 0){
        const dist = days.shift();
        let cnt = 1;
        while (days.length !== 0){
            const nextDay = days[0];
            if (nextDay <= dist){
                days.shift();
                cnt += 1;
            }
            else break
        }
        answer.push(cnt);
    }
    return answer;
}

console.log(solution([93, 30, 55],[1, 30, 5]))
