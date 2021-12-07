# 2021.05.21. Baekjoon algorithm problem #1697
# 숨바꼭질

import sys, collections
input = sys.stdin.readline

N,K = map(int,input().split())

def bfs(N,K):
    visit = []
    Q = collections.deque()
    Q.append(N)
    visit.append(N)
    time = -1

    while Q:
        Q_l = len(Q)
        time += 1
        while Q_l!=0:
            Q_l -= 1
            v = Q.popleft()
            if v == K:
                return time
            for next_v in [v-1,v+1,v*2]:
                if next_v >= 0 and next_v not in visit and next_v<100001:
                    visit.append(next_v)
                    Q.append(next_v)

        
print(bfs(N,K))



