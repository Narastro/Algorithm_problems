# 2021.02.05. Baekjoon algorithm problem # 2581
# Program for finding Prime number
# If there is none, it will print -1

M=int(input())
N=int(input())
s=[]

for i in range(M,N+1):      # range M~N
    if i==2:
        s.append(i)         # 2 is handled seperately
    for j in range(2,i):    # Sieve of Eratosthenes
        if i%j==0:
            break
        elif j==i-1:
            s.append(i)
if len(s)==0:               # -1
    print(-1)
else:
    print(sum(s))           # prime number's sum
    print(min(s))           # prime number's minmum