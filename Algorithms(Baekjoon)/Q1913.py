# 2021.10.18. 2021 Baekjoon algorithm problem #1913
# 달팽이

N = int(input())
target = int(input())
table = [[0]*N for _ in range(N)]
table[0][0] = N**2
location = []

i = N**2
x, y = 0, 0
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
k = 0
n = N-1
remain = n
while i > 0:
    x += dx[k]
    y += dy[k]
