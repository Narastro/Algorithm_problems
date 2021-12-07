# 2021.04.19. 2021 Programmers High score kit
# Camouflage

from collections import defaultdict
def solution(clothes):
    # 1. Making dress table
    dress = defaultdict(list)
    for name,kind in clothes:
        dress[kind].append(name)
    # 2. Multiply each kind+1.
    answer = 1
    for kind in dress:
        answer *= len(dress[kind]) +1
    # 3. Except nothing wear.
    return answer-1
