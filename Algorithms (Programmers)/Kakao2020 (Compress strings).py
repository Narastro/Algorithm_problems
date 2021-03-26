# 2021.03.25. 2021 KAKAO Blind Recruitment
# Compressing strings

def solution(s):
    LENGTH = len(s)
    length = []
    # exception
    if LENGTH == 1:
        return 1

    # cut_size : by length
    for cut_size in range(1, LENGTH + 1):
        splited = [s[i:i + cut_size] for i in range(0, LENGTH, cut_size)]
        LENGTH_SPLIT = len(splited)
        cnt = 0
        sub_length = LENGTH
        # comparing splited_strings
        for j in range(LENGTH_SPLIT - 1):
            if splited[j] == splited[j + 1]:
                cnt += 1
                if j == LENGTH_SPLIT - 2:
                    sub_length -= cnt * cut_size - len(str(cnt + 1))
            else:
                if cnt > 0:
                    sub_length -= cnt * cut_size - len(str(cnt + 1))
                    cnt = 0

        length.append(sub_length)

    answer = min(length)
    return answer