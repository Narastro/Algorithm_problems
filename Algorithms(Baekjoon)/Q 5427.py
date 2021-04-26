# 2021.04.26. Baekjoon algorithm problem #5427
# Fire

import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

# 상근이가 움직이는 BFS 함수
def bfs(i,j):
    time = 0
    Q.append((i,j))
    discovered[j][i] = 1
    while Q:
        fire()
        time += 1
        Q_len = len(Q)
        while Q_len:
            Q_len -= 1
            x,y = Q.popleft()
            if x == 0 or x == w-1 or y == 0 or y == h-1:
                return time

            for k in range(4):
                x_n = x + dx[k]
                y_n = y + dy[k]
                if 0 <= x_n < w and 0 <= y_n < h and discovered[y_n][x_n] == 0 and\
                    building[y_n][x_n] == '.':
                    Q.append((x_n,y_n))
                    discovered[y_n][x_n] = 1
    return -1

# 불이 번지는 BFS 함수
def fire():
    Q_fire_len = len(Q_fire)
    while Q_fire_len:
        Q_fire_len -= 1
        x,y = Q_fire.popleft()
        for k in range(4):
            x_n = x + dx[k]
            y_n = y + dy[k]
            if 0 <= x_n < w and 0 <= y_n < h and discovered[y_n][x_n] == 0 and\
                    building[y_n][x_n] != '#':
                Q_fire.append((x_n,y_n))
                discovered[y_n][x_n] = 1
    return 


T = int(input())
for _ in range(T):
    w,h = map(int,input().split())
    building = [list(map(str,input().rstrip())) for _ in range(h)]
    Q, Q_fire = deque(), deque()
    discovered = [[0]*w for _ in range(h)]
    # 불과 상근이의 위치를 찾고 큐에 저장
    for i in range(w):
        for j in range(h):
            if building[j][i] == '@':
                building[j][i] = '.'
                start = (i,j)
            elif building[j][i] == '*':
                Q_fire.append((i,j))
    
    result = bfs(start[0],start[1])

    if result == -1:
        print('IMPOSSIBLE')
    else:
        print(result)
  

