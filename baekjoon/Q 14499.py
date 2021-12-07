# 2021.05.18. Baekjoon algorithm problem #14499
# 주사위 굴리기

import sys
input = sys.stdin.readline


def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def dire(direction):
    if direction == 1:
        return 0, 1
    elif direction == 2:
        return 0, -1
    elif direction == 3:
        return -1, 0
    elif direction == 4:
        return 1, 0


n, m, x, y, k = map(int, input().split())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
com = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]
for i in com:
    a, b = dire(i)
    if 0 <= x + a < n and 0 <= y + b < m:
        x += a
        y += b
        move(i)
        if s[x][y] != 0:
            dice[1] = s[x][y]
            s[x][y] = 0
        else:
            s[x][y] = dice[1]
        print(dice[6])
