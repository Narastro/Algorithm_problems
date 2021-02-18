# 2021.02.18. leetcode algorithm problem #561
# Array partition

def Array_part_sum(nums:list[int])->int:
    return sum(sorted(nums)[::2])

nums=[1,4,3,2]
print(Array_part_sum(nums))