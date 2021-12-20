# 2021.12.20 Codility Train - Stack & Queue
# Fish

def solution(A, B):
    n = len(A)
    rev_fish = 0
    answer = 0
    for i in range(n):
        if B[i] == 0:
            if rev_fish == A[i]:
                continue
            elif rev_fish < A[i]:
                answer += 1
                rev_fish = 0
        else:
            rev_fish = A[i]

    if rev_fish != 0:
        answer += 1
    return answer


print(solution([1, 1], [1, 0]))
