# 2021.08.19. 2021 Baekjoon algorithm problem #16236
# 아기 상어


'''
<풀이 아이디어>
1) BFS로 갈 수 있는 경로 찾기(이때 크기가 같은 곳도 지나갈 수 있음)
2) BFS탐색하면서 먹을 수 있는 물고기도 탐색해줌
3) 먹을 수 있는 물고기를 거리순으로 min heap을 써서 가장 가까운 곳 찾기
4) 이때 (거리,y좌표,x좌표)로 힙에 넣어주어서 y좌표가 더 빠른 물고기를 먼저 먹음
'''

import heapq
from collections import deque,defaultdict

dx,dy = [0,1,-1,0],[1,0,0,-1]

N = int(input())
space = [list(map(int,input().split())) for _ in range(N)]
for j in range(N):
    for i in range(N):
        if space[j][i]==9:
            x = i
            y = j
            space[j][i] = 0
baby_size = 2
remain = 2

def search_bfs(x,y,size):
    queue = deque()
    visit = defaultdict(int)
    queue.append((x,y))
    visit[(x,y)] = 0
    answer = []
    while queue:
        i,j= queue.popleft()
        n = visit[(i,j)]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<N and 0<=ny<N and (nx,ny) not in visit and space[ny][nx]<=size:
                if space[ny][nx] != 0 and space[ny][nx]<size:
                    answer.append((n+1,nx,ny))
                visit[(nx,ny)] = n+1
                queue.append((nx,ny))

    return answer


def size_check(size,remain):
    remain -= 1
    if remain == 0:
        size += 1
        remain = size
    return size,remain

def min_path(queue):
    heap = []
    for d,i,j in queue:
        heapq.heappush(heap,(d,j,i))

    min_val = heapq.heappop(heap)
    space[min_val[1]][min_val[2]] = 0
    return min_val[0],min_val[2],min_val[1]
    

time = 0
while True:
    Q = search_bfs(x,y,baby_size)
    if len(Q)==0:
        break

    move,x,y = min_path(Q)
    time += move
    baby_size,remain = size_check(baby_size,remain)


print(time)


