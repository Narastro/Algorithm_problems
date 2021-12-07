# 2021.04.20. Baekjoon algorithm problem #1260
# DFS, BFS

from collections import defaultdict

graph = defaultdict(list)

N,M,V = map(int,input().split())
for _ in range(M):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)

discovered = []
def dfs_recur(v):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            dfs_recur(w)
    return
dfs_recur(V)

def dfs_stack(v):
    discovered =[]
    stack =[v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in sorted(graph[v],reverse=True):
                stack.append(w)
    return discovered

def bfs(v):
    discovered = []
    stack = [v]
    while stack:
        v = stack.pop(0)
        if v not in discovered:
            discovered.append(v)
            for w in sorted(graph[v]):
                stack.append(w)
    return discovered

# print(*discovered)
print(*dfs_stack(V))
print(*bfs(V))


