# 2021.03.04. Baekjoon algorithm problem #2606
# Virus

import sys
import collections

def virus(N:int, computer:dict)->int:
    visited=[]

    # DFS function
    def DFS(start,computer):
        # for every node
        for i in computer[start]:
            if i not in visited:
                visited.append(i)
                DFS(i,computer)
    DFS(1,computer)
    return len(visited)-1       # excepting computer#1

computer = collections.defaultdict(list)

N= int(input())
for _ in range(int(input())):
    a,b = map(int,sys.stdin.readline().split())
    computer[a].append(b)
    computer[b].append(a)

print(virus(N,computer))