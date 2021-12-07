# 2021.04.22. Baekjoon algorithm problem #16953
# A -> B

from collections import deque

def bfs(start,end):
    queue = deque()
    queue.append((start,1))
    while queue:
        v,cnt = queue.popleft()
        if v == end:
            return cnt
        v_2 = v*2
        v_1 = int(str(v)+'1')
        if v_2 <= end:
            queue.append((v_2, cnt+1))
        if v_1 <= end:
            queue.append((v_1, cnt+1))
    return -1
        

A,B = map(int,input().split())
print(bfs(A,B))

