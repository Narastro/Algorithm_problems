# 2021.06.13. Baekjoon algorithm problem #9376
# 탈옥

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    h,w = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(h)]