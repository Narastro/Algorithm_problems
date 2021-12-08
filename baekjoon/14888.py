# 2021.02.15. Baekjoon algorithm problem #14888
# Insert Operator
# source : https://claude-u.tistory.com/371

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiple, division = map(int, input().split())

operation_list = []
operation_list += [1] * plus
operation_list += [2] * minus
operation_list += [3] * multiple
operation_list += [4] * division

operation_set = []
for numbers in list(permutations(operation_list)):
    operation_set.append(numbers)
operation_set = list(set(operation_set))

max_answer = -1000000001
min_answer = 1000000001
for case in operation_set:
    answer = A[0]

    for i in range(N - 1):
        if case[i] == 1:
            answer += A[i + 1]
        elif case[i] == 2:
            answer -= A[i + 1]
        elif case[i] == 3:
            answer *= A[i + 1]
        elif case[i] == 4:
            if answer < 0:
                answer = -(-answer // A[i + 1])
            else:
                answer //= A[i + 1]


    if answer < min_answer:
        min_answer = answer
    if answer > max_answer:
        max_answer = answer

print(max_answer)
print(min_answer)