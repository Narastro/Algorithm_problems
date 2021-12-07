# 2021.03.08. Leetcode algorithm problem #787
# Cheapest Flights within K Stops

import collections, heapq

def find_cheapest_price(n:int, flights:list[list[int]], src:int, dst:int, K:int)->int:
    graph = collections.defaultdict(list)
    # graph configuration
    for u,v,w in flights:
        graph[u].append((v,w))

    # Qeueu variable: [(price, node, number of stopover remaining)]
    Q = [(0, src, K)]

    # # determine cheapest price to node based on priority queue's minimum
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0 :
            for v,w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1