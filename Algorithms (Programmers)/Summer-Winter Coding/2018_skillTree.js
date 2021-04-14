// 2021.04.14. Summer-Winter coding(2018)
// Skill tree

function solution(skill, skill_trees) {
    let answer = 0;
    
    for(let i=0;i<skill_trees.length;i++){
        const skillArray = skill.split('');
        
        for(let j=0 ; j<skill_trees[i].length ; j++){
            if (skillArray.includes(skill_trees[i][j])){
                if (skill_trees[i][j] !== skillArray.shift()){
                    break;
                }
            }
            if (j===skill_trees[i].length-1){
                answer += 1;
            }
        }
    }
    return answer;
}

console.log(solution('CBD',["BACDE", "CBADF", "AECB", "BDA"]))