# 2021.06.15. Baekjoon algorithm problem #1937
# 욕심쟁이 판다

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


dx,dy=[0,0,1,-1],[1,-1,0,0]

def dfs(i,j,N):
    if dp[j][i]:
        return dp[j][i]

    dp[j][i] = 1

    for k in range(4):
        x,y = i+dx[k], j+dy[k]
        if 0<=x<N and 0<=y<N:
            if table[j][i] < table[y][x]:
                dp[j][i] = max(dp[j][i],dfs(x,y,N)+1)
    return dp[j][i]

N = int(input())
table = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
max_val = 0
for j in range(N):
    for i in range(N):
        max_val = max(max_val,dfs(i,j,N))
print(max_val)