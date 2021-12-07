# 2021.05.17. Baekjoon algorithm problem #13458
# 시험 감독

import sys, math
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B,C = map(int, input().split())

answer = 0

for i in range(len(A)):
    if A[i] <= B:
        answer += 1
    else:
        answer += math.ceil((A[i]-B)/C)+1

print(answer)
