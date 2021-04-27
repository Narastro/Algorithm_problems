/* 2021.04.27. 2021 Programmers High score kit
 * A truck passing a bridge
 */

function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    const bridge = [];
    
    bridge.push(truck_weights.shift());
    time += 1;
    while (!bridge[0].includes(undefined)) {
        console.log(bridge)
        time += 1;
        if (bridge.length === bridge_length){
            bridge.shift();
        }

        if (bridge.reduce((a,b)=>a+b,0)+truck_weights[0] > weight){
            bridge.push(0);
        }else{
            bridge.push(truck_weights.shift());
        }
    }
    
    return time;
}

console.log(solution(2,10,[7,4,5,6]));