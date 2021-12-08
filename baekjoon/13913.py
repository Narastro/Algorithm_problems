# 2021.04.25. Baekjoon algorithm problem #13913
# Hide and seek 4


import sys
from collections import deque

input = sys.stdin.readline


def bfs(N, K):
    Q = deque()
    Q.append('/'+str(N))
    visit = [0]*100001
    visit[N] = 1
    flag = True
    time = -1
    if N > K:
        time = N-K
        v = [i for i in range(N, K-1, -1)]
        return time, v

    while flag:
        time += 1
        Q_len = len(Q)
        while Q_len != 0:
            Q_len -= 1
            v_str = Q.popleft()
            v = v_str.split('/')

            if int(v[-1]) == K:
                flag = False
                break

            for next_v in [int(v[-1])-1, int(v[-1])+1, 2*int(v[-1])]:
                if 0 < next_v and next_v < 100001 and visit[next_v] == 0:
                    visit[next_v] = 1
                    Q.append(v_str+'/'+str(next_v))

    return time, v


N, K = map(int, input().split())
time, path = bfs(N, K)
print(time)
print(*path)

