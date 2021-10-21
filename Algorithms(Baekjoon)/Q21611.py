# 2021.10.19. 2021 Baekjoon algorithm problem #21611
# 마법사 상어와 블리자드

import sys
import re
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

table = [list(map(str, input().split())) for _ in range(N)]
attacks = [list(map(int, input().split())) for _ in range(M)]

score = [0, 0, 0]


def blizard_attack(N, d, s):
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]
    x, y = N//2, N//2
    for _ in range(s):
        x += dx[d-1]
        y += dy[d-1]
        table[y][x] = '0'


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
            if table[y][x] != '0':
                Q.append(str(table[y][x]))
        dir = (dir + 1) % 4
        cnt -= 1

        if cnt == 0:
            n += 1
            cnt = 2

    for _ in range(n-1):
        x += dx[dir]
        y += dy[dir]
        if table[y][x] != '0':
            Q.append(str(table[y][x]))

    return Q


def remove_overlap(string, num):
    return re.sub(num*4+"+", "", string)


def explosion(queue):
    pre_queue = ''.join(queue)
    new_queue = deque()

    while True:
        l = len(pre_queue)
        after1_Q = remove_overlap(pre_queue, '1')
        after1 = len(after1_Q)
        score[0] += l-after1
        after2_Q = remove_overlap(pre_queue, '2')
        after2 = len(after2_Q)
        score[1] += 2*(l-after2)
        after3_Q = remove_overlap(pre_queue, '3')
        after3 = len(after3_Q)
        score[2] += 3*(l - after3)

        new_queue = re.sub('1111+|2222+|3333+', "", pre_queue)

        if l == len(new_queue):
            return deque(new_queue)
        else:
            pre_queue = new_queue


def changeQueue(queue):
    cnt = 1
    num = 0
    if queue:
        num = queue.popleft()
    new_queue = deque()
    while queue:
        this_num = queue.popleft()
        if this_num != num:
            new_queue.append(str(cnt))
            new_queue.append(num)
            cnt = 1
            num = this_num
        else:
            cnt += 1

    if num != 0:
        new_queue.append(str(cnt))
        new_queue.append(num)

    return new_queue


def arrange_table(N):
    queue = get_table_item(N)
    queue = explosion(queue)
    queue = changeQueue(queue)
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
                table[y][x] = '0'
                continue
            table[y][x] = queue.popleft()
        dir = (dir + 1) % 4
        cnt -= 1

        if cnt == 0:
            n += 1
            cnt = 2

    for _ in range(n-1):
        x += dx[dir]
        y += dy[dir]
        if not queue:
            table[y][x] = '0'
            continue
        table[y][x] = queue.popleft()


for d, s in attacks:
    blizard_attack(N, d, s)
    arrange_table(N)
print(sum(score))
