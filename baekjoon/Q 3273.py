# 2021.02.18. Baekjoon algorithm problem #3273
# Two sum

import sys
N=int(input())
nums=list(map(int,sys.stdin.readline().split()))
target=int(input())

Nums={}
cnt=0
for i,num in enumerate(nums):       # using dictionary-check
    if target-num in Nums:
        cnt += 1
    Nums[num]=i
print(cnt)

