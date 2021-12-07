# 2021.04.24. Baekjoon algorithm problem #1806
# Subsum

N, S = map(int, input().split())
A = list(map(int, input().split()))

#먼저 0~n까지의 합을 구해줌
sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    sum_A[i] = sum_A[i-1] + A[i-1]

#투포인터 설정
answer = 1000001
start = 0
end = 1

#알고리즘 실행
while start != N:
    if sum_A[end] - sum_A[start] >= S:
        if end - start < answer:
            answer = end - start
        start += 1

    else:
        if end != N:
            end += 1
        else:
            start += 1

#답이 없을 경우 & 있을 경우
if answer != 1000001:
    print(answer)
else:
    print(0)
