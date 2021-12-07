# 2021.03.08. Baekjoon algorithm problem #1966
# Printer Queue

import sys, collections

tests = int(input())
for _ in range(tests):
    N, M = map(int, sys.stdin.readline().split())
    documents = list(map(int,sys.stdin.readline().split()))
    # Queue
    Q = collections.deque(documents)
    count = 0

    while Q:
        # M is 0 (handle exception)
        if M == 0:
            a = Q.popleft()
            if Q and max(Q) > a:
                M = len(Q)
                Q.append(a)
            else:
                count += 1
                Q = collections.deque()
        # Queue operation
        else:
            for i in range(M+1):
                a = Q.popleft()
                if Q and max(Q) > a:
                    if i == M:
                        M = len(Q)
                        Q.append(a)
                    else: Q.append(a)
                elif i == M:
                    count += 1
                    Q = collections.deque()
                else:
                    count += 1
    print(count)