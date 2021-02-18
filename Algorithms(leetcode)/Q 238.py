# 2021.02.18. leetcode algorithm problem #238
# Product of Array Except Self
# No division, time complexity O(n)

def product_Except(nums:list[int])->list[int]:
    out = []
    p = 1
    # multiplication from left
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # multiplication from left result to right values
    for i in range(len(nums)-1, 0-1, -1):
        out[i]=out[i]*p
        p = p * nums[i]
    return out

nums=[1,2,3,4]
print(product_Except(nums))
