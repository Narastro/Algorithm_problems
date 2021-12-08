# 2021.02.16. Baekjoon algorithm problem #10844
# Easy stairs

N=int(input())
A=[0]+[1]*9
B=[0]*10

for _ in range(2,N+1):
    B[0]=A[1]; B[9]=A[8]
    for i in range(1,9):
        B[i]=A[i-1]+A[i+1]
    A=B[:]

print(sum(A)%1000000000)