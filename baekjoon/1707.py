# 2021.06.03. Baekjoon algorithm problem #1707
# 이분 그래프

import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def isBipartieGraph(V,graph):
    visit = [False]*(V+1)
    for i in range(1,V+1):
        if not visit[i]:
            Q = deque()
            Q.append((i,0))
            div = [[i],[]]
            while Q:
                v,group = Q.popleft()
                for node in graph[v]:
                    if node in div[group]:
                        return 'NO'
                    elif node not in div[1-group]:
                        visit[node] = True
                        div[1-group].append(node)
                        Q.append((node,1-group))

    return 'YES'


T = int(input())
for _ in range(T):
    graph = defaultdict(list)
    V,E = map(int,input().split())
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(isBipartieGraph(V,graph))
