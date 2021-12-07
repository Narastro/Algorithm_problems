# 2021.04.02. 2019 KAKAO Blind Recruitment
# Candidate Key

from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    # 1. Total Number of cases
    total = []
    for k in range(1,n_col+1):
        total.extend(combinations(range(n_col),k))
    # 2. Number of cases satisfied with uniqueness
    unique = []
    for pair in total:
        # 2-1. Determine whether there are duplicate values in each case
        tmp = [tuple([item[i] for i in pair]) for item in relation]
        if len(set(tmp)) == n_row:
            unique.append(pair)
    # 3. Number of cases satisfied with minimuality
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
                ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))