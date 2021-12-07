# 2021.02.10. Baekjoon algorithm problem #11650
# Align Coordinates 2

import sys

N=int(sys.stdin.readline())
cord=list()

for i in range(N):
    cord.append(sys.stdin.readline().split())

cord.sort(key=lambda x:(int(x[1]),int(x[0])))       # sort by y and x coordinates

for i in range(N):
    print(*cord[i])