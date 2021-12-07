# 2021.05.30. Baekjoon algorithm problem #10026
# 적록색약

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx,dy = [0,0,1,-1],[1,-1,0,0]

def dfs(i,j,N,color):
    if picture[j][i] == '#':
        return

    picture[j][i] = '#'

    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0<=x<N and 0<=y<N and picture[y][x]==color:
            dfs(x,y,N,color)

def RG_dfs(i,j,N,color):
    if RG_picture[j][i] == '#':
        return

    RG_picture[j][i] = '#'

    for k in range(4):
        x = i+dx[k]
        y = j+dy[k]
        if 0<=x<N and 0<=y<N and RG_picture[y][x]==color:
            RG_dfs(x,y,N,color)



N = int(input())
picture = [list(input().rstrip()) for _ in range(N)]
RG_picture = []
for i in range(N):
    RG_picture.append(list(''.join(picture[i]).replace('R','G')))
cnt = 0
RG_cnt = 0

for i in range(N):
    for j in range(N):
        if picture[j][i] !='#':
            dfs(i,j,N,picture[j][i])
            cnt +=1
        if RG_picture[j][i] !='#':
            RG_dfs(i,j,N,RG_picture[j][i])
            RG_cnt +=1

print(cnt,RG_cnt)