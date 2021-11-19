# 2021.11.19. Baekjoon algorithm problem #1753
# 최단 거리

# input을 readline으로 바꿔줬을 뿐인데 통과라니...흠

from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
nodes = defaultdict(list)
dist = defaultdict(int)
for i in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append((v, w))

heap = [(0, start)]
while heap:
    weight, node = heapq.heappop(heap)
    if node not in dist:
        dist[node] = weight
        for v, w in nodes[node]:
            heapq.heappush(heap, (weight+w, v))

for i in range(1, V+1):
    if i != start and dist[i] == 0:
        print('INF')
    else:
        print(dist[i])
