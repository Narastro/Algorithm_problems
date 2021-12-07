// 2021.04.20. 2021 Programmers High score kit
// An Finished Runner


function solution(participant, completion) {
    const partMap = new Map();
    const compMap = new Map();
    let answer = '';
    
    participant.forEach(function(x){
        partMap.set(x,(partMap.get(x)||0)+1);
    })

    completion.forEach(function(x){
        compMap.set(x,(compMap.get(x)||0)+1);
    })

    for (let [key,value] of partMap){
        if (compMap.get(key)!==value){
            answer = key;
        }
    }

    return answer
};

console.log(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))