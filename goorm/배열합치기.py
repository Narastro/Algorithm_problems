# 2021.12.20. goorm level
# 배열 합치기

from collections import deque

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = []

a = deque(A)
b = deque(B)
for num in a:
    if b[-1] <= num:
        answer.append(str(b.pop()))
    else:
        answer.append(str(num))
print(' '.join(answer))
