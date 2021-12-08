# 2021.03.08. Baekjoon algorithm problem #10866
# Deque

import sys, collections
Deque = collections.deque()

N = int(input())
for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push_back':
        Deque.append(commands[1])
    if commands[0] == 'push_front':
        Deque.appendleft(commands[1])
    if commands[0] == 'pop_front':
        if not len(Deque):
            print(-1)
        else:
            print(Deque.popleft())
    if commands[0] == 'pop_back':
        if not len(Deque):
            print(-1)
        else:
            print(Deque.pop())
    if commands[0] == 'size':
        print(len(Deque))
    if commands[0] == 'empty':
        if not len(Deque):
            print(1)
        else:
            print(0)
    if commands[0] == 'front':
        if not len(Deque):
            print(-1)
        else:
            print(Deque[0])
    if commands[0] == 'back':
        if not len(Deque):
            print(-1)
        else:
            print(Deque[-1])