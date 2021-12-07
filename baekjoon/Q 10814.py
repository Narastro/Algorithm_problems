# 2021.02.10. Baekjoon algorithm problem #10814
# Sort by age

import sys

N=int(sys.stdin.readline())
mem=[]

for i in range(N):
    mem.append(sys.stdin.readline().rstrip().split())

mem.sort(key=lambda x:int(x[0]))       # word is sorted by age
for i in range(N):
    print(*mem[i],sep=' ')
