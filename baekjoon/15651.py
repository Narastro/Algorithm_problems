# 2021.02.12. Baekjoon algorithm problem #15651
# N and M 3 (backtracking)

N, M = map(int, input().split())
result = []

def solve(depth, n, m):         # using back tracking
    # print when no longer need to find value
    if depth == m:
        print(*result)
    else:
        for i in range(N):
            result.append(i+1)
            solve(depth+1, n, m)    # using recursive function
            result.pop()    # when the loop is over, remove the values

solve(0, N, M)