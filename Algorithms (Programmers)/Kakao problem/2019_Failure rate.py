# 2021.04.01. 2019 KAKAO Blind Recruitment
# Failure Rate

from collections import Counter
def solution(N, stages):
    answer = []
    # 1. Initialization
    challengers = len(stages)
    count_fail = Counter(stages)    # collections.Counter
    failure_rate = [[0,i] for i in range(N+1)] # (failure_rate,stage_number)
    # 2. For each stage number
    for i in range(1,N+1):
        if i in count_fail:
            # 2-1. Calculating failure_rate
            failure_rate[i] = [count_fail[i]/challengers,i]
            challengers -= count_fail[i]
    # 2-2. Delete Unnecessary 0 Index
    failure_rate = failure_rate[1:]
    # 3-1. Sort descending by Failure rate and increasing by number
    failure_rate.sort(key=lambda x:(1-x[0],x[1]))
    # 3-2. Return only numeric indexes among result values
    for w in failure_rate:
        answer.append(w[1])
    return answer

print(solution(5,	[2, 1, 2, 6, 2, 4, 3, 3]))