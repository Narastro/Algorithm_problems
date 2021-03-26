# 2021.03.17. Baekjoon algorithm problem #7576
# Tomato

import sys,collections

read = lambda : sys.stdin.readline().split()

M,N = map(int, read())
tomatos = [list(map(int,read())) for _ in range(N)]
queue = collections.deque()

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            queue.append([i,j])

while queue:
    row, col = queue.popleft()

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for k in range(4):
        row_next = row + dx[k]
        col_next = col + dy[k]

        if 0 <= row_next < N and 0 <= col_next < M and tomatos[row_next][col_next] == 0:
            tomatos[row_next][col_next] = tomatos[row][col] + 1
            queue.append([row_next, col_next])

result = -2

check_tomato = False

for i in tomatos:
    for j in i:
        if (j == 0):
            check_tomato = True
        result = max(result, j)

if check_tomato:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)