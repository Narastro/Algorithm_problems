from collections import defaultdict


def find_head(tree, start):
    cur = start
    while tree[cur] != cur:
        cur = tree[cur]
    return cur


def solution(n, costs):
    answer = 0
    trees = defaultdict(int)
    for i in range(n):
        trees[i] = i

    connected = 0
    for cost in sorted(costs, key=lambda x: x[2]):
        if connected == n-1:
            break
        node_a = cost[0]
        node_b = cost[1]
        if find_head(trees, node_a) != find_head(trees, node_b):
            trees[find_head(trees, node_a)] = find_head(trees, node_b)
            answer += cost[2]

    return answer
