# 2021.03.08. Leetcode algorithm problem #743
# Network Delay Time

import collections, heapq

def network_delay_time(times:list[list[int]], N:int, K:int)->int:
    graph = collections.defaultdict(list)
    # graph configuration
    for u,v,w in times:
        graph[u].append((v,w))
    # variable Q [(required time, node)]
    Q = [(0,K)]
    dist = collections.defaultdict(int)

    # insert shortest path to node based on priority queue's minimum
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v,w, in graph[node]:
                alt = time + w
                heapq.heappush(Q,(alt,v))
    # whether every node have shortest path
    if len(dist) == N:
        return max(dist.values())
    return -1

