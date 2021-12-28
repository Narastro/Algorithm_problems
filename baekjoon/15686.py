# 2021.12.28. Baekjoon algorithm problem #15686
# 치킨 배달

from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
table = []
homes = []
chickens = []
for j in range(N):
    row = list(map(int, input().split()))
    for i in range(N):
        if row[i] == 1:
            homes.append((i, j))
        elif row[i] == 2:
            chickens.append((i, j))
    table.append(row)


def chicken_dist(i, j, combs):
    min_val = sys.maxsize
    for x, y in combs:
        min_val = min(min_val, abs(x-i) + abs(y-j))
    return min_val


answer = sys.maxsize
for combs in list(combinations(chickens, M)):
    sub_sum = 0
    for i, j in homes:
        sub_sum += chicken_dist(i, j, combs)
    answer = min(answer, sub_sum)
print(answer)
