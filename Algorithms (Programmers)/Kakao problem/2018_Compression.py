# 2021.04.12. 2018 KAKAO Blind Recruitment
# Compression

from collections import defaultdict
def solution(msg):
    table = defaultdict(int)
    # 1. Making index table
    for i, v in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        table[v] = i + 1
    # Initialization
    last_idx = 26
    idx = 1
    answer = []
    letter = msg[0]

    while idx < len(msg):
        # Find w
        if letter + msg[idx] not in table:
            answer.append(table[letter])
            last_idx += 1
            table[letter + msg[idx]] = last_idx
            letter = msg[idx]
            idx += 1
            continue

        letter += msg[idx]
        idx += 1
    answer.append(table[letter])
    return answer

print(solution('KAKAO'))