# 2021.12.20 Codility Train
# Max Counter

def solution(N, A):
    answer = [0]*N
    max_val = 0
    max_counter = 0
    for index in A:
        if index == N+1:
            max_counter = max_val
        else:
            if answer[index-1] < max_counter:
                answer[index-1] = max_counter+1
            else:
                answer[index-1] += 1
            max_val = max(max_val, answer[index-1])
    for i, v in enumerate(answer):
        if v < max_counter:
            answer[i] = max_counter
    return answer


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
