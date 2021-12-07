# 2021.04.30. Baekjoon algorithm problem #11659
# Subsum 4

import sys
input = sys.stdin.readline
N, M = map(int,input().split())
N_list = list(map(int,input().split()))
sub_sum = [0]*len(N_list)
sub_sum[0] = N_list[0]
for i in range(1,len(N_list)):
    sub_sum[i] += N_list[i] + sub_sum[i-1]

for _ in range(M):
    i,j = map(int,input().split())
    if i==1:
        print(sub_sum[j-1])
    else:
        print(sub_sum[j-1]-sub_sum[i-2])
