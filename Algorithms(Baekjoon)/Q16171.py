# 2021.10.07. Baekjoon algorithm problem #16171
# 비밀번호 발음하기

'''
쉽게 생각해
'''

from collections import deque

s = input()
target = input()
S = []

for letter in s:
    if not letter.isnumeric():
        S.append(letter)

if target in ''.join(S):
    print(1)
else:
    print(0)
