# 2021.03.31. 2018 KAKAO Blind Recruitment
# News clustering

from collections import defaultdict

def solution(str1, str2):
    # 1. using defaultdict of int type
    str1_dict = defaultdict(int)
    str2_dict = defaultdict(int)
    # 2. Capitalize and save 2 alphabet letters in str1,2
    for i in range(len(str1) - 1):
        if str1[i:i + 2].isalpha():
            str1_dict[str1[i:i + 2].upper()] += 1
    for j in range(len(str2) - 1):
        if str2[j:j + 2].isalpha():
            str2_dict[str2[j:j + 2].upper()] += 1
    # 3. In case of null set
    if not str1_dict.keys() and not str2_dict.keys():
        return 65536


    inter = 0
    sum_s = sum(str1_dict.values())+sum( str2_dict.values())
    # 4. calculating intersection set
    for key in str1_dict:
        if key in str2_dict:
            # 4-1. Select a small value from the common key.
            inter += min(str1_dict[key], str2_dict[key])
    # 5. calculating sum set
    sum_s -= inter
    # 6. Processing results
    answer = int((inter - sum_s) * 65536)
    return answer

print(solution('FRANCE','french'))