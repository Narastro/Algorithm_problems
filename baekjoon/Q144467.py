# 2021.10.24. Baekjoon algorithm problem #144467
# 소가 길을 건너간 이유 1

from collections import defaultdict

N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]
info = defaultdict(bool)
answer = 0

for cow, loc in inputs:
    if cow not in info:
        info[cow] = loc
    elif info[cow] != loc:
        info[cow] = loc
        answer += 1

print(answer)
