# 2021.06.23. Baekjoon algorithm problem #14502
# 연구소

import sys,copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

def bfs(walls,table,virus):
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    virus_area = 0
    Q = deque()
    for v in virus:
        Q.append(v)
    for x,y in walls:
        table[y][x] = 1

    while Q:
        v,w = Q.popleft()

        for k in range(4):
            x = v + dx[k]
            y = w + dy[k]
            if 0<=x<M and 0<=y<N and table[y][x] == 0:
                virus_area += 1
                table[y][x] = 2
                Q.append((x,y))
    return virus_area

def find_wall(area,blank,virus):
    min_val = sys.maxsize
    walls_list = list(combinations(blank,3))
    for walls in walls_list:
        min_val = min(min_val,bfs(walls,copy.deepcopy(area),virus))
    return min_val

N,M = map(int,input().split())
area = []
blank = []
virus = []
for j in range(N):
    ii = list(map(int,input().split()))
    area.append(ii)
    for i in range(M):
        if ii[i] == 0:
            blank.append((i,j))
        if ii[i] == 2:
            virus.append((i,j))
total_area = len(blank)
print(total_area - 3 - find_wall(area,blank,virus))
