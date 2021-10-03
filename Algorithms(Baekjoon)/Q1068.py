# 2021.10.03. Baekjoon algorithm problem #1068
# 트리

'''
<풀이 아이디어>
1. DFS를 이용해서 리프노드를 찾자
2. (이 문제의 예외처리) 만약 지우고자 하는 노드가 부모 노드의 하나뿐인 자식이라면 
  부모가 리프 노드가 되므로 갯수 셀 때 +1을 해주자
'''

import sys
from collections import defaultdict
input = sys.stdin.readline

def find_leaf_num(root,target,tree):
    num_leaf_nodes = 0
    stack = []
    stack.append(root)
    while stack:
        v = stack.pop()
        if v not in tree:
            num_leaf_nodes += 1
        else:
            for next_node in tree[v]:
                if next_node == target and len(tree[v])==1:
                    num_leaf_nodes += 1
                if next_node != target:
                    stack.append(next_node)
    return num_leaf_nodes


N = int(input())
leaves = list(map(int,input().split()))
tree = defaultdict(list)
for index,leaf in enumerate(leaves):
    if leaf == -1:
        root = index
        continue
    tree[leaf].append(index)
rm_leaf = int(input())
print(find_leaf_num(root,rm_leaf,tree))


