# 2021.04.23. Baekjoon algorithm problem #13549
# Hide and seek 3

from collections import deque
MAX_SIZE = 100001

def bfs(start,end):
    Q = deque()
    Q.append((start,0))
    visited = dict()

    while Q:
        v,time = Q.popleft()
        visited[v] = time

        if v == end:
            return time
            
        v_2 = v * 2
        if v_2 < MAX_SIZE and v_2 not in visited:
            Q.appendleft((v_2, time))
            visited[v_2] = time

        for dv in [v-1,v+1]:
            if dv not in visited and 0<=dv<MAX_SIZE:
                Q.append((dv,time+1))
                visited[dv] = time + 1

        

N,K = map(int,input().split())
print(bfs(N,K))


