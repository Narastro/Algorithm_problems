
number='456'

def solution(numbers):
    import itertools

    N = len(numbers)
    M = 10 ** N
    num = [1] * M
    num[0] = 0
    num[1] = 0
    num[4] = 0
    for i in range(5, M):
        for j in range(2, int(M ** (0.5))):
            if i % j == 0:
                num[i] = 0
    A = set()
    B = []
    answer = 0
    for n in range(N):
        B.append(list(itertools.permutations(numbers)))
        for w in range(len(B[n])):
            A.add(int(''.join(B[n][w])))
    K = len(A)
    for i in range(K):
        if num[A.pop()] == 1:
            answer += 1

    return answer,A

print(solution(number))