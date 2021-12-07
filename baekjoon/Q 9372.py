# 2021.06.01. Baekjoon algorithm problem #9372
# 상근이의 여행

from collections import defaultdict
import sys
input = sys.stdin.readline

def min_flight(N,flight):
    return N-1


T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    flight = defaultdict(list)
    for _ in range(M):
        a,b = map(int,input().split())
        flight[a].append(b)
        flight[b].append(a)
    
    print(min_flight(N,flight))
