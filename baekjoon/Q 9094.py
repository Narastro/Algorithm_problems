# 2021.04.26. Baekjoon algorithm problem #9094
# Mathematical Curiosity

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    cnt = 0
    for a in range(1,n-1):
        for b in range(a+1,n):
            if (a**2+b**2+m)%(a*b) == 0:
                cnt += 1
    print(cnt)
