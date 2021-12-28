# 2021.11.12. Baekjoon algorithm problem #14938
# 서강그라운드

from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(R)]
graph = defaultdict(list)

for info in infos:
    graph[info[0]].append((info[1], info[2]))
    graph[info[1]].append((info[0], info[2]))


def dijkstra(start):
    heap = []
    visit = defaultdict(bool)
    cnt_item = 0

    heapq.heappush(heap, (0, start))
    visit[start] = True
    cnt_item += items[start-1]

    while heap:
        length, node = heapq.heappop(heap)
        for next, dist in graph[node]:
            new_length = length + dist
            if new_length <= M:
                if not visit[next]:
                    cnt_item += items[next-1]
                visit[next] = True
                heapq.heappush(heap, (new_length, next))
    return cnt_item


answer = 0
for i in range(1, N+1):
    answer = max(answer, dijkstra(i))
print(answer)
