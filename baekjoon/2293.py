# 2021.12.24. Baekjoon algorithm problem #2293
# 동전 1

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
dp = [0]*(K+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, K+1):
        dp[i] += dp[i-coin]
print(dp[K])
