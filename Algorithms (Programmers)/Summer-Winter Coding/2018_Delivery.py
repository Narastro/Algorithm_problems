# 2021.04.15. Summer-Winter coding(2018)
# Delivery

from collections import defaultdict
import heapq

def solution(N, road, K):
    # 1. Set up graph
    graph = defaultdict(list)
    for i,j,w in road:
        graph[i].append([j,w])
        graph[j].append([i,w])
    # 2. Dijkstra Algorithm (using priority queue)
    # 2-1. starting point
    Q = [(0,1)]
    visit = defaultdict(int)
    # 3. Shortest path
    while Q:
        dist, node = heapq.heappop(Q)
        # 3-1. Added to 'visit' with shortest path only
        if node not in visit:
            visit[node] = dist
            for v,w in graph[node]:
                # 3-2. Do not add to queue if distance exceeds K
                if dist + w <= K:
                    heapq.heappush(Q,(dist+w,v))

    return len(visit)