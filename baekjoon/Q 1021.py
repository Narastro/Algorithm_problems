# 2021.03.08. Baekjoon algorithm problem #1021
# Rotationg Queue

import sys, collections

N,M = map(int,input().split())
li = [i for i in range(1,N+1)]
# Qr is right rotation, Ql is left rotation
Qr = collections.deque(li)
Ql = collections.deque(li)
nums = collections.deque(map(int, sys.stdin.readline().split()))
count = 0

while nums:
    num = nums.popleft()
    if Qr[0] == num :
        Qr.popleft()
        # copy Qr to Ql
        Ql = collections.deque(list(Qr)[:])
        continue
    else:
        for i in range(N+1):
            Qr.rotate(-1)
            Ql.rotate()
            count += 1
            # if it finds first, copy the value
            if Qr[0] == num:
                Qr.popleft()
                Ql = collections.deque(list(Qr)[:])
                break
            elif Ql[0] == num:
                Ql.popleft()
                Qr = collections.deque(list(Ql)[:])
                break

print(count)