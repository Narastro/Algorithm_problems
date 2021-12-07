# 2021.05.06. 2020 KAKAO winter internship
# Jewerlry Shopping

from collections import defaultdict
import sys
def solution(gems):
    answer = [0,0]
    # 종류 갯수 찾기
    kind = {}
    for j in gems:
        kind[j] = 1
    n = len(kind)
    # 투포인터를 이용한 풀이
    min_val = sys.maxsize
    start, end = 0,0
    cnt_dict = defaultdict(int)
    while start<len(gems) and end <= len(gems):
        if len(cnt_dict) == n:
            if min_val > end-start+1 :
                min_val = end-start+1
                answer[0] = start
                answer[1] = end-1
            cnt_dict[gems[start]] -= 1
            if cnt_dict[gems[start]] == 0:
                del cnt_dict[gems[start]]
            start += 1
        else:
            if end == len(gems):
                break
            cnt_dict[gems[end]] += 1
            end += 1
    # 인덱스 맞춰주기
    answer[0] += 1
    answer[1] += 1
    return answer


print(solution(["A","A","B"]))
