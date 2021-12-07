# 2021.02.11. Baekjoon algorithm problem #15649
# N and M 1 (backtracking)


N, M = map(int, input().split())
visited = [False] * N           # visit point check
result = []

def solve(depth, n, m):         # using back tracking
    # print when no longer need to find value
    if depth == m:
        print(*result)
    else:
        for i in range(N):
            if not visited[i]:  # for unvisited value
                visited[i] = True
                result.append(i+1)
                solve(depth+1, n, m)    # using recursive function
                visited[i] = False
                result.pop()    # when the loop is over, remove the values

solve(0, N, M)
