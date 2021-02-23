# 2021.02.23. Baekjoon algorithm problem #17298
# A big number

import sys

N = int(input())
sequence = list(map(int,sys.stdin.readline().split()))

stack = []
# default value
answer = [-1] * N

for i, cur in enumerate(sequence):
    # Replace value if the current value is greater than stack value
    while stack and cur > sequence[stack[-1]]:
        last = stack.pop()
        answer[last] = cur
    stack.append(i)
print(*answer)