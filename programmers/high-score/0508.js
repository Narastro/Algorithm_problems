

function solution(weights, head2head){
    let winRate = head2head.map((rate,i)=>rate.split('').filter(s=>s==='W').length);
    let heavWin = head2head.map((rate,i)=>rate.split('').filter((s,j)=>weights[j]>weights[i]&&s==='W').length);
    let answer = weights.map((weight,index)=>({
        weight:weight, win:head2head[index], index:index, winRate:winRate[index], heavWin:heavWin[index]
    }))
    .sort((a,b)=>{
        if(a.winRate !== b.winRate) return b.winRate-a.winRate;
        if(a.heavWin !== b.heavWin) return b.heavWin-a.heavWin;
        if(a.weight !== b.weight) return b.weight-a.weight;
        a.index-b.index;
    })

    return answer.map(t=>t.index+1);
}






console.log(Math.min(1,2));