/* 2021.04.27. 2021 Programmers High score kit
 * A truck passing a bridge
 */

function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    // bridge라는 큐 선언
    const bridge = [];
    // 첫 트럭을 큐에 넣음
    bridge.push(truck_weights.shift());
    time += 1;
    // 큐에 아무런 값이 없을때까지 while 반복
    while (bridge.findIndex(e => e===undefined) !== 0) {
        time += 1;

        if (bridge.length === bridge_length){
            bridge.shift();
        }
        // 다리의 무게를 초과한 경우 0을 삽입
        if (bridge.reduce((a,b)=>a+b,0)+truck_weights[0] > weight){
            bridge.push(0);
        }else{
            bridge.push(truck_weights.shift());
        }
    }
    
    return time;
}

console.log(solution(2,10,[7,4,5,6]));