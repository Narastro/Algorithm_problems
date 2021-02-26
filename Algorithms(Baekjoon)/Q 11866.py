# 2021.02.26. Baekjoon algorithm problem #11866
# Josephus problem

N, K = map(int, input().split())
stack = [i for i in range(1, N + 1)]
result = []
temp = K - 1

for i in range(N):
    if len(stack) > temp:
        result.append(stack.pop(temp))
        temp += K - 1
    elif len(stack) <= temp:
        temp = temp % len(stack)
        result.append(stack.pop(temp))
        temp += K - 1

print('<',end='')
print(*result,sep=', ',end='')
print('>')