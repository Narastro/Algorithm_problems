# 2021.06.20. Baekjoon algorithm problem #13460
# 구슬 탈출 2

from collections import deque
n, m = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
table = []
def move(i, j, dx, dy):
    distance = 0
    while table[i + dx][j + dy] != "#" and table[i][j] != "O":
        i += dx
        j += dy
        distance += 1
    return i, j, distance
def bfs():
    while q:
        ri, rj, bi, bj, d = q.popleft()
        if d > 10:
            break
        for i in range(4):
            nri, nrj, r_d = move(ri, rj, dx[i], dy[i])
            nbi, nbj, b_d = move(bi, bj, dx[i], dy[i])
            if table[nbi][nbj] != "O":
                if table[nri][nrj] == "O":
                    print(d)
                    return
                if nri == nbi and nrj == nbj:
                    if r_d > b_d:
                        nri -= dx[i]
                        nrj -= dy[i]
                    else:
                        nbi -= dx[i]
                        nbj -= dy[i]
                if not visit[nri][nrj][nbi][nbj]:
                    visit[nri][nrj][nbi][nbj] = True
                    q.append([nri, nrj, nbi, nbj, d + 1])
    print(-1)
for i in range(n):
    a = list(input())
    table.append(a)
    for j in range(m):
        if a[j] == "R":
            ri, rj = i, j
        if a[j] == "B":
            bi, bj = i, j
q = deque()
q.append([ri, rj, bi, bj, 1])
visit[ri][rj][bi][bj] = True
bfs()