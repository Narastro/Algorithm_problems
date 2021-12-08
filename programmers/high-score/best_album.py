# 2021.04.19. 2021 Programmers High score kit
# Best album

from collections import defaultdict

def solution(genres, plays):
    # 1. Initialization
    table = defaultdict(list)
    cnt_table = defaultdict(int)
    answer = []
    # 2. Making table and count_table
    for i, genre in enumerate(genres):
        table[genre].append((plays[i], i))
        cnt_table[genre] += plays[i]
    # 3. Sort by play count
    for genre, play in sorted(cnt_table.items(), key=lambda x: x[1], reverse=True):
        # 3-1. Condition3
        s = sorted(table[genre], key=lambda x: (x[0], -x[1]))
        # Two or less
        for i in range(len(s)):
            if i == 2:
                break
            answer.append(s.pop()[1])

    return answer
