# 2021.02.09. Baekjoon algorithm problem #2751
# To sort numbers 2nd


import sys

N=int(sys.stdin.readline())
num=[]
for i in range(N):
    num.append(int(sys.stdin.readline()))
print(*sorted(num),sep='\n')