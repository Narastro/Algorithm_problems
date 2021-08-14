# 2021.08.15. 2021 Baekjoon algorithm problem #14503
# 로봇 청소기

'''
<풀이 아이디어>
1) 4방향
2) 청소는 2로 나타냄
'''


dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
location = [list(map(int, input().split())) for _ in range(N)]


def change_dir(d):
    return (d+3) % 4


def already_clean(x, y):
    cleaned = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or location[ny][nx] != 0:
            cleaned += 1
    return cleaned == 4


def front(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < M and 0 <= ny < N and location[ny][nx] == 0:
        return nx, ny

    else:
        return False


def reverse(x, y, d):
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    if nx < 0 or nx >= M or ny < 0 or ny >= N or location[ny][nx] == 1:
        return False

    for _ in range(2):
        d = change_dir(d)
    return d


while True:
    print(r, c)
    location[r][c] = 2
    if already_clean(c, r):
        if not reverse(c, r, d):
            break
        d = reverse(c, r, d)
        if not front(c, r, d):
            c, r = front(c, r, d)
    else:
        d = change_dir(d)
        if not front(c, r, d):
            continue
        c, r = front(c, r, d)

answer = 0
for j in range(N):
    for i in range(M):
        if location[j][i] == 2:
            answer += 1

print(answer)
