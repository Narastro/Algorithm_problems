# 2021.06.23. Baekjoon algorithm problem #14502
# 연구소

'''
쉽게 해결하려다 낭패본 문제,
벽을 세울 수 있는 모든 경우의 수를 브루트포스로 계산했다.
일단 combination을 사용해 빈 칸 중에 벽을 세울 수 있는 모든 경우의 수를 구하고,
그 경우의 수마다 BFS를 이용해 바이러스가 퍼지는 영역의 넓이를 계산해서
총 빈칸의 갯수 - 벽 3개의 수 - 바이러스 퍼진 넓이 = 안전영역
으로 답을 구했다.
'''

import sys,copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 바이러스가 퍼지는 넓이를 구하는 BFS
def bfs(walls,table,virus):
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    virus_area = 0
    Q = deque()
    # 바이러스
    for v in virus:
        Q.append(v)
    # 벽 설치
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

# 벽을 세우는 모든 경우의 수
def find_wall(area,blank,virus):
    min_val = sys.maxsize   # 여기서 min을 이용한 이유는 바이러스가 최소한 퍼지는 영역을 구하기 위함이다.
    walls_list = list(combinations(blank,3))
    # 각 경우마다 bfs를 호출해 가장 적게 퍼지는 영역을 구했다.
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
