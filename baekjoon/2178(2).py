# 2021.04.21. Baekjoon algorithm problem #2178
# Labyrinth Navigation

from collections import deque

# 1. 데크를 이용한 BFS
def bfs(i,j):
    # 1-1. 상하좌우
    dx = [1,0,0,-1]
    dy = [0,1,-1,0]
    # 1-2. 초기 세팅
    Q = deque()
    Q.append([0,0])
    # 1-3. 큐를 이용
    while Q:
        v,w = Q.popleft()
        # 1-4. 상하좌우 값중 1인 값에 현재 이동거리를 입력
        for i in range(4):
            if 0 <= v+dx[i] <M and 0 <= w+dy[i] < N and\
                table[w+dy[i]][v+dx[i]] == 1:
                Q.append([v+dx[i],w+dy[i]])
                table[w+dy[i]][v+dx[i]] = table[w][v]+1

N,M = map(int, input().split())
table = [list(map(int,input())) for _ in range(N)]

bfs(0,0)

print(table[-1][-1])


