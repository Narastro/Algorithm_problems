# 2021.06.03. Leetcode algorithm problem #53
# Maximum Subarray


import sys
def solution(nums):
    best_sum = sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num,current_sum+num)
        best_sum = max(best_sum,current_sum)

    return best_sum