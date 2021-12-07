# 2021.02.22. Baekjoon algorithm problem #10773
# Zero that out

import sys

N = int(input())

stack = []
for _ in range(N):
    commands = int(sys.stdin.readline())
    if commands == 0:
        stack.pop()
    else:
        stack.append(commands)

print(sum(stack))