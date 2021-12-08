# 2021.10.05. Baekjoon algorithm problem #12865
# 평범한 배낭

'''
주의할 것!
- 이전 dp가 000000인 경우 고려해줄 것!
'''


N, K = map(int, input().split())
itemList = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for j in range(1, len(itemList)+1):
    weight = itemList[j-1][0]
    value = itemList[j-1][1]
    for i in range(K+1):
        if i < weight:
            dp[j][i] = dp[j-1][i]
        else:
            dp[j][i] = max(dp[j-1][i], dp[j-1][i-weight]+value)
    # print(dp)

print(dp[-1][-1])
