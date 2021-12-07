# 2021.09.18. 2021 Programmers High score kit - DP
# N으로 표현

def solution(N, number):
    # 같은 경우, 경우의 수는 1개
    if N == number:
        return 1

    numbers = [set() for x in range(8)]  # 1~8개의 갯수로 만들어질 수 있는 숫자들

    for i, x in enumerate(numbers, start=1):  # 인덱스 시작을 1부터
        x.add(int(str(N) * i))

    for i in range(1, 8):   # numbers를 돌며 만들어질 수 있는 경우의 수 모두 구함
        for j in range(i):
            for op1 in numbers[j]:
                for op2 in numbers[i-j-1]:
                    numbers[i].add(op1 + op2)
                    numbers[i].add(op1 - op2)
                    numbers[i].add(op1 * op2)
                    if op2 != 0:
                        numbers[i].add(op1 // op2)

        if number in numbers[i]:  # 찾으면 리턴
            answer = i + 1
            break

    else:
        answer = -1

    return answer
