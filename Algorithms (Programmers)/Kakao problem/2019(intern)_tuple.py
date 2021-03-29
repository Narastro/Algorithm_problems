# 2021.03.29. 2019 KAKAO winter internship
# Tuple

def solution(s):
    # 1. create a list(int) of s
    # 1-1. slicing string
    s = s[2:-2]
    s = s.split('},{')
    # 1-2. convert to integer
    list_s = []
    for j in s:
        if ',' in j:
            list_s.append(list(map(int,j.split(','))))
        else: list_s.append([int(j)])
    # 2. sort by length
    list_s.sort(key=lambda x:len(x))
    # 3. put in the results in order
    answer = []
    for nums in list_s:
        for num in nums:
            if num in answer:
                continue
            answer.append(num)
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))