# 2021.02.16. Baekjoon algorithm problem #1003
# Fibonacci function

import sys
# input
N=int(sys.stdin.readline())
n=[]
for i in range(N):
    n.append(int(sys.stdin.readline()))
# Create Fibonacci sequence in advance
num=[[0,0]]*41
num[0]=[1,0]
num[1]=[0,1]
for i in range(2,40+1):
    num[i]=[num[i-2][0]+num[i-1][0],num[i - 2][1] + num[i - 1][1]]
# output
for i in range(N):
    print(*num[n[i]])