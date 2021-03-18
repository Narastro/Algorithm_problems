# 2021.03.18. Leetcode algorithm problem #239
# Sliding Window Maximum

import collections, sys

def max_sliding_window(nums: list[int], k:int)->list[int]:
    result =[]
    window = collections.deque()
    current_max = -sys.maxsize
    for i, v in enumerate(nums):
        window.append(v)
        # the size of sliding window, k
        if i < k-1:
            continue

        # new value is bigger than existing maximum value
        if current_max == -sys.maxsize:
            current_max = max(window)
        elif v > current_max:
            current_max = v

        result.append(current_max)

        # if maximum value is out, initialization
        if current_max == window.popleft():
            current_max = -sys.maxsize
    return result

