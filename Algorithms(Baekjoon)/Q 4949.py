# 2021.02.23. Baekjoon algorithm problem #4949
# The balance of the World

import sys

table = {
    ')' : '(',
    ']' : '['
}

while True:
    stack = []
    answer = True
    sequence = sys.stdin.readline().rstrip()
    # Termination condition
    if sequence == '.':
        break
    for char in sequence:
        # in case of (, [
        if char == '(' or char == '[':
            stack.append(char)
        # in case of ),], Exception processing(No stack)
        elif char == ')' or char == ']':
            if not stack or table[char] != stack.pop():
                answer = False
    # print
    if answer == True and len(stack)==0:
        print('yes')
    else:
        print('no')
