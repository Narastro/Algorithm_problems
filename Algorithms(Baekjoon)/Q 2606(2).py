# 2021.04.22. Baekjoon algorithm problem #2606
# Virus

from collections import defaultdict
computers = defaultdict(list)

def dfs_stack(start):
    stack = [start]
    discovered = [start]
    while stack:
        v = stack.pop()
        for w in computers[v]:
            if w not in discovered:
                discovered.append(w)
                stack.append(w)

    return len(discovered)-1



N = int(input())
k = int(input())

for _ in range(k):
    x,y = map(int,input().split())
    computers[x].append(y)
    computers[y].append(x)

print(dfs_stack(1))




