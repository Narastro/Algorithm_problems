# 2021.06.11. Baekjoon algorithm problem #5014
# 스타트링크

from collections import deque,defaultdict

def bfs(F,S,G,U,D):
    visit = defaultdict(int)
    visit[S] = 0
    Q = deque()
    Q.append(S)

    while Q:
        v = Q.popleft()

        if v == G:
            return visit[v]

        for nv in [v+U,v-D]:
            if nv not in visit and 1<=nv<=F:
                visit[nv] = visit[v]+1
                Q.append(nv)

    return 'use the stairs'

F,S,G,U,D = map(int,input().split())
print(bfs(F,S,G,U,D))