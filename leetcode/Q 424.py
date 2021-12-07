# 2021.04.29. Leetcode algorithm problem #424
# Longest Repeating Character Replacement

import collections
def solution(s,k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1,len(s)+1):
        counts[s[right-1]] += 1
        #가장 흔한 문자 탐색
        max_char_n = counts.most_common(1)[0][1]

        # 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left
    # 최댓길이는 for문 끝날때까지 유지되므로
