# 2021.06.04. Baekjoon algorithm problem #14620
# 꽃길

import sys
input = sys.stdin.readline
dx,dy = [1,-1,0,0],[0,0,1,-1]

def openFlower(lst):
    find = []
    ans = 0

    for f in lst:
        x = f % N
        y = f // N
        find.append((x,y))
        for w in range(4):
            xn = x+dx[w]
            yn = y+dy[w]
            if xn<0 or xn>=N or yn<0 or yn>=N:
                return sys.maxsize
            find.append((xn,yn))

    if len(set(find))==15:
        for i,j in find:
            ans += flower[j][i]
        return ans
    return sys.maxsize
N = int(input())
flower = [list(map(int,input().split())) for _ in range(N)]
min_val = sys.maxsize
for i in range(N**2):
    for j in range(N**2):
        for k in range(N**2):
            if i!=j and j!=k:
                min_val = min(min_val,openFlower([i,j,k]))

print(min_val)