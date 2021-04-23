/* 2021.04.22. 2021 Programmers High score kit
 * Camouflage
 */

function solution(clothes) {
    let answer = 1;
    const map = new Map();
    for(let [dress,kind] of clothes){
        if(map.get(kind)){
            map.set(kind,map.get(kind)+1)
        }else{
        map.set(kind,1);
        }
    }
    for(let kind of map.keys()){
        console.log(kind)
        answer *= map.get(kind)+1;
    }

    return answer-1;
}

console.log(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))