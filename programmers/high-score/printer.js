/* 2021.05.06. 2021 Programmers High score kit
 * Printer
 */

function solution(priorities, location) {
    let cnt = 1;
    let maxVal = Math.max.apply(null,priorities)
    while(priorities.length !==0){
        v = priorities.shift();
        location -= 1
        if (v === maxVal){
            if(location === 0){
                return cnt
            }else{
                cnt += 1
                maxVal = Math.max.apply(null,priorities)
                continue;
            }
        }
        else if(location===0){
            location = priorities.length;
            priorities.push(v)

        }

    }

    return cnt
}

console.log(solution([1,1,9,1,1,1],0))