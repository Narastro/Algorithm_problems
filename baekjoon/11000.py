# 강의실 배정

import sys,heapq
input = sys.stdin.readline

N = int(input()) # 3
classes = [list(map(int,input().split())) for _ in range(N)] # [[1,3],[2,4],[3,5]]

classes.sort()
heap = []
max_room = 0

for cla in classes:
    max_room = max(max_room,len(heap))
    if not heap or heap[0]>cla[0]: # 강의실이 비거나 강의가 아직 안 끝난 경우
        heapq.heappush(heap,cla[1])
    elif heap and heap[0]<=cla[0]: # 강의가 끝난 경우
        heapq.heappop(heap)
        heapq.heappush(heap,cla[1])
print(max_room)