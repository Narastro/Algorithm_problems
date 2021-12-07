# 2021.04.22. Baekjoon algorithm problem #14226
# Imoticon

from collections import deque

def bfs(target):
    Q = deque()
    Q.append((1,0))
    visited = dict()
    visited[(1,0)] = 0
    while Q:
        v,clip = Q.popleft()
        time = visited[(v,clip)]
        
        if v==target:
            break
        
        if v != clip and (v,v) not in visited.keys():
            Q.append((v, v))
            visited[(v,v)] = time + 1
            
        if clip != 0 and v+clip <= target and (v+clip, clip) not in visited.keys():
            Q.append((v+clip, clip))
            visited[(v+clip, clip)] = time + 1

        if 0 < v-1 and (v-1, clip) not in visited.keys():
            Q.append((v-1, clip))
            visited[(v-1, clip)] = time + 1

    return time

S = int(input())
print(bfs(S))
