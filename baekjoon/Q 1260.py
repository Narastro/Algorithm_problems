# 2021.03.02. Baekjoon algorithm problem #1260
# DFS and BFS

import sys

# DFS using recursive function
def DFS(v,discovered=[]):
    discovered.append(v)
    for i in range(1,N+1):
        if not i in discovered and matrix[v][i]:
            discovered = DFS(i,discovered)
    return discovered

# BFS using Queue
def BFS(start):
    dicovered = [start]
    queue = [start]
    while queue:
        v = queue.pop(0)
        for i in range(1,N+1):
            if i not in dicovered and matrix[v][i]:
                dicovered.append(i)
                queue.append(i)
    return dicovered


N,M,V = map(int, sys.stdin.readline().split())
matrix = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,sys.stdin.readline().split())
    matrix[a][b] = matrix[b][a] = 1

print(*DFS(V))
print(*BFS(V))



