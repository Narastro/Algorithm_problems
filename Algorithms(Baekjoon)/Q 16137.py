# 2021.06.14. Baekjoon algorithm problem #16137
# 견우와 직녀

import sys
from collections import deque,defaultdict
input = sys.stdin.readline
dx,dy = [0,1,0,-1],[1,0,-1,0]

def isAcross(x,y,N):
    v,p = False,False
    for k in [0,2]:
        i = x+dx[k]
        j = y+dy[k]
        if 0<=i<N and 0<=j<N and table[j][i] != 1:
            v = True
    for k in [1,3]:
        i = x+dx[k]
        j = y+dy[k]
        if 0<=i<N and 0<=j<N and table[j][i] != 1:
            p = True

    if v and p:
        return True
    else:
        return False


def bfs(N,M):
    Q = deque()
    Q.append((0,0,0,False,False))
    visit = defaultdict(int)
    visit[(0,0)] = 1

    while Q:
        v,w,time,flag,across = Q.popleft()
        if v==N-1 and w==N-1:
            return time
        if table[w][v]== 1:
                Q.append((v,w,time+1,flag,across))

        for k in range(4):
            x = v+dx[k]
            y = w+dy[k]
            if 0<=x<N and 0<=y<N and (x,y) not in visit:
                # 일반도로
                if table[y][x]==1:
                    Q.append((x,y,time+1,flag,False))
                    visit[(x,y)]=1
                # 새로운 오작교
                elif table[y][x] == 0 and not flag and not across:
                    if time > 0 and (time+1)%M == 0 and not isAcross(x,y,N):
                        Q.append((x,y,time+1,True,True))
                        visit[(x,y)] = 1
                # 기존 오작교
                elif time > 0 and table[y][x] > 1 and not across and time%(table[y][x]-1)==0:
                    Q.append((x,y,time+1,flag,True))
                    visit[(x,y)] = 1

N,M = map(int,input().split())
table = [list(map(int,input().split())) for _ in range(N)]
print(bfs(N,M))
