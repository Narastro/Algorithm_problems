# 2021.02.12. Baekjoon algorithm problem #15650
# N and M 2 (backtracking)

N,M = map(int,input().split())

visit=[False]*N         # visit point check
result=[]

def solve(depth,n,m):   # using back tracking
    # print when no longer need to find value
    if depth==m:
        print(*result)
    else:
        for i in range(n,len(visit)):
            if not visit[i]:
                visit[i]=True
                result.append(i+1)
                solve(depth+1,i+1,m)        # using recursive function
                visit[i]=False
                result.pop()

solve(0,0,M)