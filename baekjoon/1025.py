# 2021.12.20. Baekjoon algorithm problem #1025
# 제곱수 찾기

import math

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
max_val = -1
dx, dy = [1, 1,  -1, -1], [-1, 1, -1, 1]


def order_table(x, y, dir, x_size, y_size, length):
    num = ''
    if x_size == 0 and y_size == 0:
        return int(table[y][x])

    while 0 <= x < M and 0 <= y < N and length != 0:
        num += table[y][x]
        x += x_size * dx[dir]
        y += y_size * dy[dir]
        length -= 1
    return int(num)


def is_total_square(num):
    if math.floor(math.sqrt(num))**2 == num:
        return True
    return False


def find_total_square(max_v, number):
    if is_total_square(number):
        max_v = max(max_v, number)
    return max_v


for j in range(N):
    for i in range(M):
        for dir in range(4):
            for x_size in range(0, M):
                for y_size in range(0, N):
                    for length in range(1, max(N, M)+1):
                        number = order_table(i, j, dir, x_size, y_size, length)
                        max_val = find_total_square(max_val, number)

print(max_val)
