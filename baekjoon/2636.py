# 2021.11.12. Baekjoon algorithm problem #2636
# 치즈

from collections import deque, defaultdict

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]


def bfs(i, j):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    queue = deque()
    queue.append((i, j))
    cheese_cnt = 0
    while queue:
        x, y = queue.popleft()
        if table[y][x] == 1:
            table[y][x] = 0
            cheese_cnt += 1
            continue
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visit:
                queue.append((nx, ny))
                visit[(nx, ny)] = True
    return cheese_cnt


last_cheese = 0
cheese = 1
time = 0
while cheese != 0:
    visit = defaultdict(bool)
    cheese = 0
    for j in range(N):
        for i in range(M):
            if j == 0 or j == N-1 or i == 0 or i == M-1:
                if not visit[(i, j)] and table[j][i] == 0:
                    cheese += bfs(i, j)
    if cheese == 0:
        break
    time += 1
    last_cheese = cheese
print(time)
print(last_cheese)
