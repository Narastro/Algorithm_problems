# 2021.02.08. Baekjoon algorithm problem #10872
# Factorial

N=int(input())
S=1
while N!=0:
    S=S*N
    N-=1
print(S)