# 2021.09.18. 2021 Programmers High score kit - DP
# 정수삼각형

# 풀이
# 맨 가장자리는 그냥 이전층을 더해주고, 가운데는 둘 중의 큰 걸 더한다.

def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(i+1):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == i:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    return max(triangle[-1])
