# 2021.04.16. 2021 Programmers monthly code challenge season2
# Making all 0

from collections import defaultdict
from collections import deque


def solution(a, edges):
    # 불가능한 경우
    if sum(a) != 0:
        return -1

    # 양뱡향 그래프 구성
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # 연결된 노드가 1이고 가중치가 0이 아닌 것들로 리프노드 만들기
    leaves = deque()
    for node in graph:
        if len(graph[node]) == 1:
            leaves.append(node)

    # 각 리프노드에 대해 반복
    answer = 0

    while leaves:
        leaf = leaves.popleft()
        leaf_val = a[leaf]
        # 최종 루트노드만 남은 경우의 처리
        if not graph[leaf]:
            answer += abs(leaf_val)
            break

        next_leaf = graph[leaf].pop()
        # 연산처리
        a[leaf] = 0
        a[next_leaf] += leaf_val
        answer += abs(leaf_val)

        # 다음 노드가 리프노드가 되는 경우 leaves에 추가
        # 시간 초과를 방지하기 위한 편법으로 1000이하만 취급...
        if len(graph[next_leaf]) < 1000:
            graph[next_leaf].remove(leaf)

        if len(graph[next_leaf]) == 1:
            leaves.append(next_leaf)
    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
