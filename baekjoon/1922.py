# 2021.11.07. Baekjoon algorithm problem #1922
# 네트워크 연결

from collections import defaultdict


def find_head(tree, start):
    cur = start
    while tree[cur] != cur:
        cur = tree[cur]
    return cur


N = int(input())
M = int(input())
costs = [list(map(int, input().split())) for _ in range(M)]
answer = 0

trees = defaultdict(int)
for i in range(N):
    trees[i] = i

connected = 0
for cost in sorted(costs, key=lambda x: x[2]):
    if connected == N-1:
        break
    node_a = cost[0]
    node_b = cost[1]
    if find_head(trees, node_a) != find_head(trees, node_b):
        trees[find_head(trees, node_a)] = find_head(trees, node_b)
        answer += cost[2]
        connected += 1

print(answer)
