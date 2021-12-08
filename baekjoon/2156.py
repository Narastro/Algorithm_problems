# 2021.02.17. Baekjoon algorithm problem #2156
# Wine tasting

# input
N=int(input())
wine=[int(input()) for _ in range(N)]

# initial value
DP=[0 for _ in range(10000)]
DP[0]=wine[0]

# DP
for i in range(1,N):
    if i==1:        # N=2
        DP[1] = DP[0] + wine[1]
    elif i==2:      # N=3
        DP[2] = max(DP[0] + wine[2], wine[1] + wine[2], DP[1])
    else:           # N>3
        DP[i]=max(DP[i-3]+wine[i-1]+wine[i],
              DP[i-2]+wine[i],
              DP[i-1])
print(DP[N-1])