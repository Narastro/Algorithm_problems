# 2021.06.15. Baekjoon algorithm problem #11403
# 경로 찾기

import sys
from collections import defaultdict
input = sys.stdin.readline

#입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
    
#플로이드-워셜 알고리즘
for k in range(N): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N): 
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


#출력
for row in graph:
    for col in row:
        print(col, end = " ")
    print()