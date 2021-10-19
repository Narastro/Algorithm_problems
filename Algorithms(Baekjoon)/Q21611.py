# 2021.10.19. 2021 Baekjoon algorithm problem #21611
# 마법사 상어와 블리자드

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
attacks = [list(map(int, input().split())) for _ in range(M)]

score = [0, 0, 0]


def blizard_attack(N, d, s):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    x, y = N//2, N//2
    for i in range(s):
        x += dx[d-1]
        y += dy[d-1]
        table[y][x] = 0


def get_table_item(N):
    x, y = N//2, N//2
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 2
    n = 1
    dir = 0
    Q = deque()
    while n != N:
        for _ in range(n):
            x += dx[dir]
            y += dy[dir]
            if table[y][x] != 0:
                Q.append(str(table[y][x]))
        dir = (dir + 1) % 4
        cnt -= 1

        if cnt == 0:
            n += 1
            cnt = 2
    return Q


def remove_overlap(string, num):
    # 문자열이 들어왔을 때 4개 이상인 문자열을 없애주는 함수 짜야됨
    return


def explosion(queue):
    new_queue = queue

    while True:
        l = len(new_queue)
        new_queue = remove_overlap(''.join(new_queue), '1')
        after1 = len(new_queue)
        score[0] += l-after1
        new_queue = remove_overlap(new_queue, '2')
        after2 = len(new_queue)
        score[1] += 2*(after1-after2)
        new_queue = remove_overlap(new_queue, '3')
        score[2] += after2 - len(new_queue)

        if l == len(new_queue):
            return deque(new_queue)


def arrange_table(N):
    queue = get_table_item(N)
    queue = explosion(queue)
    print(queue)
    x, y = N//2, N//2
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 2
    n = 1
    dir = 0
    while n != N:
        for _ in range(n):
            x += dx[dir]
            y += dy[dir]
            if not queue:
                table[y][x] = 0
                continue
            table[y][x] = queue.popleft()
        dir = (dir + 1) % 4
        cnt -= 1

        if cnt == 0:
            n += 1
            cnt = 2


blizard_attack(N, 2, 2)
arrange_table(N)

print(table)
