# 2021.05.28. Baekjoon algorithm problem #3687
# 성냥개비

import sys
from itertools import product

table = {
    2:'1',
    3:'7',
    4:'4',
    5:'2',
    6:'0',
    7:'8'
}

def min_sol(N):
    ret = [8 for i in range((N+6)//7)]
    if N%7==1: ret[0]=1;ret[1]=0
    if N%7==2: ret[0]=1
    if N%7==3: ret[0]=2;ret[1]=0;ret[2]=0
    if N%7==4: ret[0]=2;ret[1]=0
    if N%7==5: ret[0]=2
    if N%7==6: ret[0]=6
    return ret


            
    
def max_sol(N):
    if N%2==0:
        return '1'*(N//2)
    else:
        return '7'+'1'*(N//2-1)


gridy = [0,0,1,7,4,2,6,8,10,18,22]

T = int(input())
for _ in range(T):
    N = int(input())
    if N<11:
        print(gridy[N],max_sol(N))
    else:
        print(*min_sol(N),sep='',end=" ")
        print(max_sol(N))
