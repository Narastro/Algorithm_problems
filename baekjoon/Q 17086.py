# 2021.04.22. Baekjoon algorithm problem #17086
# Baby Shark 2

from collections import deque

def bfs(i,j):
    Q = deque()
    Q.append((i,j,0))
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    while Q:
        x,y,dis = Q.popleft()
        if table[x][y]:
            break

        for k in range(8):
            x_n = x+dx[k]
            y_n = y+dy[k]
            if 0 <= x_n < N and 0 <= y_n < M:
                if table[x_n][y_n]:
                    dis += 1
                    Q. clear()
                    break
                else:
                    Q.append((x_n, y_n, dis+1))
    return dis
                
            

N,M = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(N)]
max_val = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            max_val = max(max_val,bfs(i,j))
print(max_val)
