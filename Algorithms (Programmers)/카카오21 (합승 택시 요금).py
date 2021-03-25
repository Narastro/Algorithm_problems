# 2021.03.25. 2021 KAKAO Blind Recruitment
# Fare of Sharing a cab

from collections import defaultdict
import heapq as h
import sys


def solution(n, s, a, b, fares):
    # making graph
    graph = defaultdict(list)
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # dijkstra algorithm
    def dijkstra(start, d):
        Q = [(0, start)]
        dist = defaultdict(int)
        # using priority queue
        while Q:
            fare, node = h.heappop(Q)
            # if arrive at a node, return fare
            if node == d:
                return fare
            if node not in dist:
                dist[node] = fare
                for v, w in graph[node]:
                    alt = fare + w
                    h.heappush(Q, (alt, v))
        # if can't arrive, return maxsize
        return sys.maxsize

    min_val = sys.maxsize
    # share a cab point k at all node
    for k in range(1, n + 1):
        ss = dijkstra(s, k) + dijkstra(k, a) + dijkstra(k, b)
        min_val = min(min_val, ss)
    answer = min_val
    return answer
