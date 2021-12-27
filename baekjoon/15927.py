# 2021.12.27. Baekjoon algorithm problem #15927
# 회문은 회문아니야!!

# 문자열을 가장한 그리디 문제 ㄷㄷ

import sys

input = sys.stdin.readline
s = list(input().rstrip())


def solution(s):
    answer = -1

    if len(s) < 2 or len(set(s)) == 1:
        return answer

    if s == s[::-1]:
        return len(s)-1

    else:
        return len(s)


print(solution(s))
