# 2021.09.18. 2021 Programmers High score kit - DP
# 도둑질

# 풀이
# 1번째부터 시작, 2번째부터 시작 각각 점화식?

def solution(money):
    answer = 0
    length = len(money)
    dp = [0]*length
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    for i in range(2, length-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])

    dp2 = [0]*length
    dp2[0] = 0
    dp2[1] = money[1]
    for i in range(2, length):
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])

    return max(max(dp), max(dp2))


print(solution([1, 2, 3, 1]))
