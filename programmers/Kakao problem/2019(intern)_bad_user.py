# 2021.05.07. 2019 KAKAO winter internship
# Bad User
from collections import defaultdict
from itertools import permutations




def dfs(n,visit):
    if n == len(cor):
        print(visit)
        answer.append(1)
        return
    
    for i in range(len(cor[n])):
        if str(cor[n][i]) not in visit:
            dfs(n+1,visit+str(cor[n][i]))


def solution(user_id, banned_id):
    global cor,answer
    cor = []
    answer = []
    for ban in banned_id:
        tmp = []
        for index,user in enumerate(user_id):
            if len(ban) != len(user):
                continue
            
            for i,v in enumerate(ban):
                if v == '*':
                    pass
                elif v != user[i]:
                    break
                
                if i==len(ban)-1:
                    tmp.append(index)
        cor.append(tmp)


    dfs(0,'')

    return len(answer)


print(solution(	["frodo", "fradi", "crodo",
      "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
