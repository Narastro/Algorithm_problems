# 2021.06.20. Baekjoon algorithm problem #13460
# 구슬 탈출 2

import sys
from collections import deque
input = sys.stdin.readline

def bfs(rx,ry,bx,by):
    print(N)

N,M = map(int,input().split())
table = [list(input().rstrip()) for _ in range(N)]

Q = deque()
for j in range(N):
    for i in range(M):
        if table[j][i] == 'R':
            rx,ry = i,j
        if table[j][i] == 'B':
            bx,by = i,j
bfs(rx,ry,bx,by)