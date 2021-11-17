# 2021.11.17. Baekjoon algorithm problem #22856
# 트리 순회

from collections import defaultdict

tree = defaultdict(list)
parent_tree = defaultdict(int)
visit = defaultdict(bool)
answer = []


def find_parent(node):
    while True:
        parent = parent_tree[node]
        if not visit[parent]:
            return parent
        else:
            node = parent


def tree_tour(start):
    left_node = tree[start][0]
    right_node = tree[start][1]
    parent_node = parent_tree[start]
    stack = [start]
    while stack:
        node = stack.pop()
        parent_node = parent_tree[node]
        answer.append(node)
        if visit[node]:
            if parent_node == 0:
                return len(answer)-1
            stack.append(parent_node)
            continue
        if node == 0:
            return len(answer)-1
        visit[node] = True
        left_node = tree[node][0]
        right_node = tree[node][1]
        if left_node != -1 and not visit[left_node]:
            stack.append(left_node)
        elif right_node != -1 and not visit[right_node]:
            stack.append(find_start(right_node))
        else:
            stack.append(parent_node)


def find_start(node):
    answer.append(node)
    while True:
        if tree[node][0] != -1:
            node = tree[node][0]
            answer.append(node)
        else:
            answer.pop()
            return node


def find_end():
    node = 1
    cnt = 0
    while True:
        if tree[node][1] == -1:
            return cnt
        cnt += 1
        node = tree[node][1]


N = int(input())
inputs = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N+1):
    tree[i] = inputs[i-1][1:]
    parent_tree[inputs[i-1][1]] = i
    parent_tree[inputs[i-1][2]] = i
if N == 1:
    print(0)
else:
    print(tree_tour(find_start(1))-find_end())
