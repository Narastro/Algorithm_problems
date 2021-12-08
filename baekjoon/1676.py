# 2021.06.15. Baekjoon algorithm problem #1676
# 팩토리얼 0의 개수

import math

N = list(str(math.factorial(int(input()))))
cnt = 0
while N.pop() == '0':
    cnt += 1
print(cnt)