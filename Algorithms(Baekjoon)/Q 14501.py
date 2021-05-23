# 2021.05.21. Baekjoon algorithm problem #14501
# 퇴사

import sys
input = sys.stdin.readline

def calcul(N,start,schedule):
    last = N
    counsel = 0
    for i in range(N):
        last -= 1
        if last > schedule[i][0]: 
        schedule[i]

N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]

