# 2021.03.29. 2021 KAKAO Blind Recruitment
# Ranking search

from collections import defaultdict
from itertools import combinations as comb
from bisect import bisect_left

def solution(infos, querys):
    # 1. create table by hash
    table = defaultdict(list)
    for info in infos:
        info_split = info.split()
        info_score = int(info_split.pop())
        # 1-1. using combinations tools
        for k in range(0, 4 + 1):
            for j in comb(info_split, k):
                table[''.join(j)].append(info_score)

    answer = []
    # 2. sort table
    for key in table.keys():
        table[key].sort()

    # 3. refine query
    for query in querys:
        query = query.split()
        query_score = int(query.pop())
        # 3-1. remove 'and'
        for _ in range(3):
            query.remove('and')
        # 3-2. remove '-'
        while '-' in query:
            query.remove('-')
        # 4. search ranking by bisect tools
        score_list = table[''.join(query)]
        N = len(score_list) - bisect_left(score_list, query_score)
        answer.append(N)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210",\
                "python frontend senior chicken 150","cpp backend senior pizza 260",\
                "java backend junior chicken 80","python backend senior chicken 50"],\
               ["java and backend and junior and pizza 100","python and frontend and \
               senior and chicken 200","cpp and - and senior and pizza 250",\
                "- and backend and senior and - 150","- and - and - and chicken 100",\
                "- and - and - and - 150"]))