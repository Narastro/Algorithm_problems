/* 2021.05.06. 2021 Programmers High score kit
 * Best Album
 */

function solution(genres, plays) {
    let answer = [];
    // 장르별로 총 플레이수를 세는 과정
    const cntMap = new Map();
    genres.forEach((genre,i) => {
        cntMap.set(genre, cntMap.get(genre)? cntMap.get(genre)+plays[i]: plays[i])
    });
    // 장르, 횟수, 인덱스를 Key로 갖는 객체 arr 형성
    const arr = genres.map((v,i)=>({
        genre:v , count:plays[i], index:i
    }));
    // 문제에 주어진대로 정렬
    arr.sort((a,b)=>{
        if(a.genre !== b.genre) return cntMap.get(b.genre) - cntMap.get(a.genre);
        if(a.count !== b.count) return b.count - a.count;
        return a.index - b.index
    });
    // 2개까지만 출력되게 filter함수 후, 인덱스만 출력하는 map 함수
    const cntGenre = new Map();
    return arr.filter((obj)=>{
        if(cntGenre.get(obj.genre) >= 2) return false;
        cntGenre.set(obj.genre,cntGenre.get(obj.genre)?cntGenre.get(obj.genre)+1:1)
        return true;
    })
    .map(t=>t.index);
}

console.log(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))