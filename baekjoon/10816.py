# 2021.02.18. Baekjoon algorithm problem #10816
# Number card 2

import sys
N=int(input())
nums=list(map(int,sys.stdin.readline().split()))
M=int(input())
Find_nums=list(map(int,sys.stdin.readline().split()))

Nums={}                 # using dictionary (searching time complexity O(1))
for i,num in enumerate(nums):
    if num in Nums:
        Nums[num]+=1
    else:
        Nums[num]=1

for i in range(M):
    if Find_nums[i] in Nums:
        print(Nums[Find_nums[i]])
    else:
        print(0)