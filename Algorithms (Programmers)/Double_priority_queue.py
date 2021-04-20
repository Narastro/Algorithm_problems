# 2021.04.20. 2021 Programmers High score kit
# Double priority queue

import heapq

def solution(operations):
    # 0. 초기화 
    answer = []
    n = 0
    min_heap = []
    max_heap = []
    # 1. 각 명령마다 반복
    for op in operations:
        command = op.split()[0]
        num = op.split()[1]
        # 1-1. 입력
        if command == 'I':
            n += 1
            heapq.heappush(min_heap,int(num))
            heapq.heappush(max_heap, -int(num))
        # 1-2. 최댓값 삭제
        elif command == 'D' and num == '1':
            if max_heap:
                n -= 1
                heapq.heappop(max_heap)
        # 1-3. 최솟값 삭제
        elif command == 'D' and num == '-1':
            if min_heap:
                n -= 1
                heapq.heappop(min_heap)
        # 1-4. 모든 값이 삭제된 경우 동기화
        if n==0:
            min_heap = []
            max_heap = []

    if n == 0:
        return [0,0]
    else:
        answer.append(-heapq.heappop(max_heap))
        answer.append(heapq.heappop(min_heap))
        return answer