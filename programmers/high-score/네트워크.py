# 2021.12.20 2021 Programmers High score kit - DFS
# 네트워크

from collections import defaultdict


def solution(n, computers):
    answer = 0
    visit = defaultdict(bool)

    def dfs(start):
        stack = [start]
        visit[start] = True
        while stack:
            v = stack.pop()
            for i, connect in enumerate(computers[v]):
                if connect == 1 and i != v and i not in visit:
                    visit[i] = True
                    stack.append(i)
        return

    for i in range(n):
        if i not in visit:
            dfs(i)
            answer += 1
    return answer
