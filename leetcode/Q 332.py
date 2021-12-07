# 2021.03.03. Leetcode algorithm problem #332
# Reconstruct Itinerary

import collections

def Recon_Itinerary(tickets:list[list[str]])->list[str]:
    graph = collections.defaultdict(list)
    # in regular order
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)

    route = []
    def DFS(a):
        while graph[a]:
            DFS(graph[a].pop())
        route.append(a)

    DFS('JFK')
    return route[::-1]