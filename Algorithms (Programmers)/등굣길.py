# 2021.09.18. 2021 Programmers High score kit - DP
# 등굣길

# 풀이
# 고딩 때 많이 풀던 길찾기 문제...

def solution(m, n, puddles):
    answer = [[0]*(m+1) for i in range(n+1)]
    answer[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue

            if [j, i] in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = answer[i-1][j]+answer[i][j-1]
    return answer[n][m] % 1000000007
