# 2021.02.16. Baekjoon algorithm problem #9461
# Wave Ban Sequence

# input
N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
# A(n)=A(n-1)+A(n-5)
sequence=[1,1,1,2,2,3,4,5,7,9]
for i in range(10,max(num)+1):
    sequence.append(sequence[i-1]+sequence[i-5])
# output
for i in range(N):
    print(sequence[num[i]-1])