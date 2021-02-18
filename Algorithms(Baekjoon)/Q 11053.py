# 2021.02.17. Baekjoon algorithm problem #1920
# Find number

import sys
N=int(input())
nums=list(map(int,sys.stdin.readline().split()))
M=int(input())
Find_nums=list(map(int,sys.stdin.readline().split()))

Nums={}                 # using dictionary (searching time complexity O(1))
for i,num in enumerate(nums):
    Nums[num]=i

for i in range(M):
    if Find_nums[i] in Nums:
        print(1)
    else:
        print(0)