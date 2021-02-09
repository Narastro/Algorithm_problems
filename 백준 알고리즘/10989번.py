# 2021.02.09. Baekjoon algorithm problem #10989
# To sort numbers 3rd

import sys

N=int(sys.stdin.readline())
m=10001             # total number
num=[0]*m
# using counting alignment
for i in range(N):
    num[int(sys.stdin.readline())]+=1
for i in range(m):
    if num[i]==0:
        pass
    else:
        print('{}\n'.format(i)*num[i],end='')