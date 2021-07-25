# 2021.04.22. Baekjoon algorithm problem #12851
# Hide-and-seek

from collections import deque
MAX_SIZE = 100001

def bfs(start,end):
    Q = deque()
    Q.append([start,0])
    method = []
    visited = [0 for _ in range(MAX_SIZE+1)]

    while Q:
        v,cnt = Q.popleft()
        visited[v] = cnt
        
        if method and method[0] < cnt:
            continue

        elif v == end:
            method.append(cnt)
            continue

        for dv in [v*2,v+1,v-1]:
            if 0<= dv <=MAX_SIZE:
                if not visited[dv] or visited[dv]>=cnt+1:
                    Q.append([dv,cnt+1])
                    visited[dv] = cnt+1

    return method[-1],len(method)

N,K = map(int,input().split())

print(*bfs(N,K),sep='\n')        


