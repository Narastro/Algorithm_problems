# 2021.10.08. Baekjoon algorithm problem #6550
# 부분 문자열

'''
쉬움
'''

import sys
from collections import deque
while True:
    s = sys.stdin.readline()
    if not s:
        break
    s = s.split()
    target = deque(s[0])

    for letter in s[1]:
        if target[0] == letter:
            target.popleft()

        if len(target) == 0:
            print('Yes')
            break
    else:
        print('No')
