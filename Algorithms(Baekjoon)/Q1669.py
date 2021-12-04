# 2021.12.04. Baekjoon algorithm problem #1669
# 멍멍이 쓰다듬기

X, Y = map(int, input().split())
N = Y-X
if N == 0:
    print(0)
else:
    n = int(N**0.5)
    if n**2 == N:
        print(2*n-1)
    else:
        k = N - n**2
        if k <= n:
            print(2*n)
        else:
            print(2*n+1)
