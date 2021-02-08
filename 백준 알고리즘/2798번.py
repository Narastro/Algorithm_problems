# 2021.02.08. Baekjoon algorithm problem #2798
# Blackjack


N,M=map(int,input().split())
num=list(map(int,input().split()))
max=0
# examine the sum of all values
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if max<num[i]+num[j]+num[k]<=M:
                max=num[i]+num[j]+num[k]
print(max)

