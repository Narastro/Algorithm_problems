# 2021.03.08. Baekjoon algorithm problem #5430
# AC

import sys, collections

T = int(input())
for _ in range(T):
    error = 0
    p = sys.stdin.readline().rstrip()
    p.replace('RR','')
    n = int(input())
    rcount = 0
    if n==0:
        s=input()
        Q=[]
    else:
        s = list(map(int,sys.stdin.readline().rstrip()[1:-1].split(',')))
        Q = collections.deque(s)
    for i in range(len(p)):
        command = p[i]
        if command == 'R':
            Q.reverse()
        elif command == 'D':
            if not Q:
                error = 1
                break
            Q.popleft()
    if error == 1:
        print('error')
    else:
        print('[',end='')
        print(*Q,sep=',',end='')
        print(']')