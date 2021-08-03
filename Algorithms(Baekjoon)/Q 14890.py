# 2021.08.07. Baekjoon algorithm problem #14890
# 경사로

N, L = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
answer = 0
flat = 0
cur = 0
for i in range(N):
    for j in range(N):
        if cur and tablep[i][j] == cur:
            flat += 1
        elif cur != table[i][j]:
            cur = table[i][j]
            flat = 0

        if (cur)
        table[i][j]
