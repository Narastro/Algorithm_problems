# 2021.02.08. Baekjoon algorithm problem #2231
# Digit Generator


import math
N=int(input())
# Case of 1
if N==1:
    print(0)
# Case of no time-out problem
elif N<19:
    for i in range(1,N):
        digit = []
        icnt = int(math.log10(i) + 1)
        for j in range(icnt):
            digit.append((i // (10 ** j) % 10))
        if i + sum(digit) == N:
            print(i)
            break
        if i == N - 1:
            print(0)
# For a large number
else:
    cnt=int(math.log10(N)+1)
    for i in range(N-(9*cnt),N):
        digit=[]
        icnt = int(math.log10(i)+1)
        for j in range(icnt):
            digit.append((i//(10**j)%10))
        if i+sum(digit)==N:
            print(i)
            break
        if i==N-1:
            print(0)