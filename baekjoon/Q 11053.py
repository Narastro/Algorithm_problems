# 2021.06.04. Baekjoon algorithm problem #11053
# 가장 긴 증가하는 부분 수열

'''
동적배열 DP를 이용해서 자신보다 작은 수의 수열의 길이에 +1을 더해주는 방식으로 계산.
'''

import sys
from typing import Sequence
input = sys.stdin.readline

N = int(input())
sequence = list(map(int,input().split()))
DP = [1]*N

for i in range(1,N):
    max_val = 0
    for w in range(i):
        if sequence[w]<sequence[i]:
            max_val = max(max_val,DP[w])
    DP[i] = max_val + 1

print(max(DP))

