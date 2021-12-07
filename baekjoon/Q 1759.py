# 2021.05.27. Baekjoon algorithm problem #1759
# 암호 만들기

import sys
from itertools import combinations
input = sys.stdin.readline

L,C = map(int,input().split())
alpha_list = list(map(str,input().split()))
answer = set()

for s in combinations(alpha_list,L):
    cnt = 0
    for m in 'aeiou':
        if m in s:
            cnt += 1
    if cnt >= 1 and L-cnt>=2:
        answer.add(''.join(sorted(s)))

print(*sorted(answer),sep='\n')
