# 2021.05.19. Baekjoon algorithm problem #14500
# 테트로미노


import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
mfinger = [[[0, 1], [0, 2], [-1, 1]], [[0, 1], [0, 2], [1, 1]],
           [[1, 0], [2, 0], [1, 1]], [[1, 0], [1, -1], [2, 0]]]
n, m = map(int, input().split())
s = []
visit = [[0] * m for i in range(n)]
result = 0


def dfs(x, y, cnt, num):
    global result
    if cnt == 4:
        result = max(result, num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visit[nx][ny] == 0:
            visit[nx][ny] = 1
            dfs(nx, ny, cnt + 1, num + s[nx][ny])
            visit[nx][ny] = 0


def middlefinger(x, y):
    global result
    for i in mfinger:
        try:
            num = s[x][y] + s[x + i[0][0]][y + i[0][1]] + \
                s[x + i[1][0]][y + i[1][1]] + s[x + i[2][0]][y + i[2][1]]
        except:
            num = 0
        result = max(result, num)


for i in range(n):
    s.append(list(map(int, input().split())))
result = 0
for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 1, s[i][j])
        visit[i][j] = 0
        middlefinger(i, j)
print(result)