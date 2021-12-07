# 2021.02.18. leetcode algorithm problem #1
# Two sum

def two_sum(nums:list[int],target:int)->list[int]:
    nums_map={}             # using dictionary
    # consolidate into one for statement
    for i,num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num]=i

print(two_sum([2,7,11,15],9))
