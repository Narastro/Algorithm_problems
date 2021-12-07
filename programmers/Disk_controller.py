# 2021.04.20. 2021 Programmers High score kit
# Disk controller

import heapq

def solution(jobs):
    # 0. 초기값 세팅
    answer,cur = 0,0
    n = len(jobs)
    heap = []
    # 1. 제일 우측에 가장 먼저 들어왔으며 짧은 작업이 오도록 정렬
    jobs.sort(key=lambda x:(x[0],x[1]),reverse=True)
    # 2. 제일 먼저 처리되는 작업이 0초가 아닌 시점에 들어온 경우
    w = jobs.pop()
    if w[0] != 0:
        cur = w[0]
    heapq.heappush(heap, (w[1], w[0]))

    # 3. 힙 자료구조 이용
    while heap:
        # 3-1. 현재 시각 cur, 걸린시간 answer
        job = heapq.heappop(heap)
        cur += job[0]
        answer += cur - job[1]
        # 3-2. 현재 시각보다 빨리 들어온 작업을 모두 힙에 넣음
        while True:
            if jobs and jobs[-1][0] <= cur:
                tmp = jobs.pop()
                heapq.heappush(heap,(tmp[1],tmp[0]))
            else:
                break
        # 3-3. 작업이 남았음에도 힙이 비어있는 경우 예외처리
        if jobs and not heap:
            tmp = jobs.pop()
            answer += tmp[0]-cur
            cur = tmp[0]
            heapq.heappush(heap, (tmp[1], tmp[0]))

    return answer // n
