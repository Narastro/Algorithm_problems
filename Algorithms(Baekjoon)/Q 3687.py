# 2021.05.28. Baekjoon algorithm problem #3687
# 성냥개비

import sys
table = {
    2:[1],
    3:[7],
    4:[4],
    5:[2,5],
    6:[0,6,9],
    7:8
}

def min_sol(N,table):
    pos = N//7
    answer = ''
    for i in range(pos):
        for k in [2,5,4,6,3,7]:
            
    
def max_sol(N):
    if N%2==0:
        return '1'*(N//2)
    else:
        return '7'+'1'*(N//2-1)



T = int(input())
for _ in range(T):
    N = int(input())
    min_val = sys.maxsize
