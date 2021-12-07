# 2021.02.23. Baekjoon algorithm problem #9012
# Parenthesis

import sys

table = {')' : '('}

N = int(input())
answer = [True]*N

for i in range(N):
    stack = []
    sequence = list(map(str,sys.stdin.readline().rstrip()))
    for char in sequence:
        # in case of (
        if char not in table:
            stack.append(char)
        # in case of ), Exception processing(No stack)
        elif not stack or table[char] != stack.pop() :
            answer[i] = False
    # print
    if answer[i] == True and len(stack)==0:
        print('YES')
    else:
        print('NO')


