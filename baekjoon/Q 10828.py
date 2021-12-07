# 2021.02.22. Baekjoon algorithm problem #10828
# Stack

import sys
stack = []

N = int(input())
for _ in range(N):
    commands = sys.stdin.readline().split()
    if commands[0] == 'push':
        stack.append(commands[1])
    if commands[0] == 'pop':
        if not len(stack):
            print(-1)
        else:
            print(stack.pop())
    if commands[0] == 'size':
        print(len(stack))
    if commands[0] == 'empty':
        if not len(stack):
            print(1)
        else:
            print(0)
    if commands[0] == 'top':
        if not len(stack):
            print(-1)
        else:
            print(stack[-1])
