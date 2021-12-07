# 2021.11.15. Baekjoon algorithm problem #1238
# 파티

from collections import defaultdict
import heapq

N, M, X = map(int, input().split())
graph_info = [list(map(int, input().split())) for _ in range(M)]
graph = defaultdict(list)
to_home = defaultdict(list)

for start, end, time in graph_info:
    to_home[end].append((start, time))
    graph[start].append((end, time))


def dijkstra(start):
    heap = [(0, start)]
    visit = defaultdict(int)

    while heap:
        time, node = heapq.heappop(heap)
        if node not in visit:
            visit[node] = time
            for next, w in graph[node]:
                heapq.heappush(heap, (time+w, next))

    return visit


max_val = 0
back = dijkstra(X)
for i in range(1, N+1):
    go = dijkstra(i)
    max_val = max(max_val, go[X]+back[i])
print(max_val)
