# 2021.02.26. Baekjoon algorithm problem #18258
# Queue 2

import sys
import collections

queue = collections.deque()

N = int(input())
for _ in range(N):
    commands = sys.stdin.readline().rstrip().split()
    if commands[0] == 'push':
        queue.append(int(commands[1]))
    elif commands[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif commands[0] == 'size':
        print(len(queue))
    elif commands[0] == 'empty':
        if len(queue)==0:
            print(1)
        else: print(0)
    elif commands[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commands[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)

