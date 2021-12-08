# 2021.04.21. Baekjoon algorithm problem #1743
# Avoid food waste

def dfs(x,y):
    stack = [(x, y)]
    cnt = 1
    while stack:
        v, w = stack.pop()
        table[v][w] = 0
        for i in range(4):
            if 0 <= v+dx[i] < N and 0 <= w+dy[i] < M and\
                    table[v+dx[i]][w+dy[i]] != 0:
                stack.append((v+dx[i], w+dy[i]))
                cnt += 1
    return cnt

N,M,K = map(int,input().split())
table = [[0 for _ in range(M)]for _ in range(N)]
for _ in range(K):
    i, j = map(int,input().split())
    table[i-1][j-1] = 1
max_val = 0
dx,dy = [0,1,-1,0],[1,0,0,-1]
for x in range(N):
    for y in range(M):
        if table[x][y]:
            max_val = max(max_val,dfs(x,y))

print(max_val)


