# 2021.04.20. 2021 Programmers High score kit
# Travel route

from collections import defaultdict


def solution(tickets):
    answer = []
    graph = defaultdict(list)

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])

    for country in graph:
        graph[country].sort()

    def dfs(start):
        stack = [start]
        while stack:
            v=stack[-1]
            if v in graph and graph[v]:
                stack.append(graph[v].pop())
            else:
                answer.append(stack.pop())
        return
    dfs("ICN")
    answer.reverse()
    return answer

print(
    solution([["ICN", "SFO"], ["ICN", "ATL"], [
             "SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
)
