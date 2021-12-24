# 2021.12.24. Baekjoon algorithm problem #2110
# 공유기 설치

import math

N, C = map(int, input().split())
pos = [int(input()) for _ in range(N)]
pos.sort()
l = len(pos)


def is_possible(gap):
    cnt = 1
    prev = pos[0]
    for i in range(1, N):
        if pos[i]-prev >= gap:
            cnt += 1
            prev = pos[i]
    if cnt >= C:
        return True
    return False


result = 0
min_gap = 1
max_gap = pos[-1] - pos[0]
while min_gap <= max_gap:
    mid = math.floor((min_gap + max_gap)/2)
    if is_possible(mid):
        result = max(result, mid)
        min_gap = mid + 1
    else:
        max_gap = mid-1

print(result)
