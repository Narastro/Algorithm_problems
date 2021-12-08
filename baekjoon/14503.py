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


def left_check(x, y, d):
    nd = (d+3) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if 0 <= nx < M and 0 <= ny < N and location[ny][nx] == 0:
        return True
    return False


def turn_left(d):
    return (d+3) % 4


def four_way_already(x, y):
    already = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N or location[ny][nx] != 0:
            already += 1
    return already == 4


def backward_pos(x, y, d):
    nd = (d+2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if nx < 0 or nx >= M or ny < 0 or ny >= N or location[ny][nx] == 1:
        return False
    return True


def turn_back(d):
    return (d+2) % 4


def go_straight(x, y, d):
    nx = x + dx[d]
    ny = y + dy[d]
    return nx, ny


def printFun():
    for j in range(N):
        print(location[j])


while True:
    # print()
    # printFun()
    location[r][c] = 2
    if four_way_already(c, r):
        if backward_pos(c, r, d):
            c, r = go_straight(c, r, turn_back(d))
            continue
        else:
            break

    if left_check(c, r, d):
        d = turn_left(d)
        c, r = go_straight(c, r, d)
        continue
    else:
        d = turn_left(d)
        continue

answer = 0
for j in range(N):
    for i in range(M):
        if location[j][i] == 2:
            answer += 1

print(answer)
