# 2021.04.16. leetcode algorithm problem #310
# Minimum Height Trees

from collections import defaultdict
def find_min_h_tree(n, edges)->list[int]:
    if n<=1:
        return [0]
    
    # Two-way graph configuration
    graph = defaultdict(list)
    for i,j in edges:
        graph[i].append(j)
        graph[j].append(i)
    
    # Initiate Leaf node
    leaves = []
    for i in range(n+1):
        if len(graph[i])==1:
            leaves.append(i)
    
    # Repeat until root is left
    while n > 2:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)

            if len(graph[neighbor]) == 1:
                new_leaves.append(neighbor)
            
        leaves = new_leaves
    return leaves

