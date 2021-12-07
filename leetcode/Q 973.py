# 2021.04.28. Leetcode algorithm problem #973
# K Closest Points to Origin

import heapq
def solution(points,K):
    heap =[]
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap,(dist,x,y))

    result = []
    for _ in range(K):
        (dist,x,y) = heapq.heappop(heap)
        result.append((x,y))
    return result

