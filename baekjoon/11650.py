# 2021.02.10. Baekjoon algorithm problem #11650
# Align Coordinates

import sys

N=int(sys.stdin.readline())
cord=list()

for i in range(N):
    cord.append(sys.stdin.readline().split())

cord.sort(key=lambda x:(int(x[0]),int(x[1])))       # sort by x and y coordinates

for i in range(N):
    print(*cord[i])