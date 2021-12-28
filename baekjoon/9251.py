# 2021.12.28. Baekjoon algorithm problem #9251
# LCS

# 기억했으면 좋은 풀이법!
# 1. 이중 배열로 만들어서 문자 각각을 비교한다.
# 2. 문자가 같으면 대각선에 있는 dp값에 1은 더하면 되고
# 3. 다르면 이전 둘 중 하나의 값 중 큰 값을 넣으면 된다.

import sys
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()
N1 = len(s1)+1
N2 = len(s2)+1
dp = [[0]*(N2) for _ in range(N1)]

for i in range(N1):
    for j in range(N2):
        if i == 0 or j == 0:
            continue
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[N1-1][N2-1])
