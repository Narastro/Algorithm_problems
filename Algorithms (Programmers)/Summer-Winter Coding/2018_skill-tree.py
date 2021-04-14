# 2021.04.14. Summer-Winter coding(2018)
# Skill tree

def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        skill_list = list(skill)
        # using python's for-else statement
        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:answer += 1

    return answer


print(solution('CBD', ["BACDE", "CBADF", "AECB", "BDA"]	))
