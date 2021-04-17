# 2021.04.16. 2021 Programmers monthly code challenge season2
# Making all 0

from collections import defaultdict
def solution(a, edges):
    if sum(a) != 0:
        return -1

    tree = defaultdict(list)
    
    for edge for edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    leaves = []
    for node in tree:
        if len(node)==1:
            leaves.append(node)
    n = len(a)
    while n > 1:
        n -= len(leaves)
        new_leaves = []
        for leaf in leaves:
            neighbor = tree[leaf].pop()

        leaves = new_leaves

    answer = -2
    return answer
