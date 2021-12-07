# 2021.06.15. Baekjoon algorithm problem #1949
# 우수 마을

'''
트리DP 연습하기 좋은 문제,
1. 우수마을로 포함되는 경우를 DP[cur][1], 아닌 경우를 DP[cur][0]으로 나누기
2. 재귀DFS를 이용
3. 방문 표시 visit을 해줘야 리프노드에서부터 DP탐색 가능하다
'''


import sys
sys.setrecursionlimit(100000)
from collections import defaultdict
input = sys.stdin.readline

def dfs(cur):
    visit[cur] = True
    DP[cur][0] = 0
    DP[cur][1] = people[cur]
    for next_node in tree[cur]:
        if not visit[next_node]:
            dfs(next_node)
            DP[cur][1] += DP[next_node][0]
            DP[cur][0] += max(DP[next_node][1],DP[next_node][0])

N = int(input())
people = [0] + list(map(int,input().split()))
visit = [False]*(N+1)
DP = [[0,0] for _ in range(N+1)]
tree = defaultdict(list)
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
dfs(1)
print(max(DP[1][0],DP[1][1]))