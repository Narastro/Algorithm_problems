# 2021.02.12. Baekjoon algorithm problem #15652
# N and M 4 (backtracking)

N,M = map(int,input().split())

result=[]

def solve(depth,n,m):   # using back tracking
    # print when no longer need to find value
    if depth==m:
        print(*result)
    else:
        for i in range(n-1,N):          # start itself
            result.append(i+1)
            solve(depth+1,i+1,m)        # using recursive function
            result.pop()

solve(0,1,M)