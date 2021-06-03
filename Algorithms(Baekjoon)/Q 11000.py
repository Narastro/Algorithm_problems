# 2021.06.03. Baekjoon algorithm problem #11000
# 강의실 배정

import sys,heapq
input = sys.stdin.readline

N = int(input())
classes = [list(map(int,input().split())) for _ in range(N)]
classes.sort()
heap = []
max_room = 0
for cla in classes:
    max_room = max(max_room,len(heap))
    if not heap or heap[0]>cla[0]:
        heapq.heappush(heap,cla[1])
    elif heap and heap[0]<=cla[0]:
        heapq.heappop(heap)
        heapq.heappush(heap,cla[1])
print(max_room)