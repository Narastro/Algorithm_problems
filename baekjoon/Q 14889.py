# 2021.02.15. Baekjoon algorithm problem #14889
# Start and link

from itertools import combinations

# input
N=int(input())
chart=[list(map(int, input().split())) for _ in range(N)]

# calculation score
def score(x:list[int])->int:
    val=0
    for i in x:
        for j in x:
            if i==j:
                continue
            val+=chart[i-1][j-1]
    return val

# number of possible team cases
possible_team=[]
member=[i for i in range(1,N+1)] # member is 1~N
for team in list(combinations(member,N//2)):        # using itertools.combinations
    possible_team.append(team)

# calculation minimum score
min_value=10000
for i in range(len(possible_team)//2):
    start=possible_team[i]
    link=possible_team[-i-1]
    min_value=min(min_value,abs(score(start)-score(link)))

print(min_value)




