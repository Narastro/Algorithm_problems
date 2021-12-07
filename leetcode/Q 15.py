# 2021.02.18. leetcode algorithm problem #15
# 3Sum

def three_Sum(nums:list[int])->list[int]:
    results=[]
    nums.sort()

    for i in range(len(nums)-2):
        # skip duplicates
        if i>0 and nums[i]==nums[i-1]:
            continue
        # using two pointer
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i]+nums[left]+nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # if sum = 0
                results.append([nums[i],nums[left],nums[right]])

                while left < right and nums[left]==nums[left+1]:
                    left+=1
                while left < right and nums[right]==nums[right-1]:
                    right-=1
                left += 1
                right -= 1
    return results

nums = [-1,0,1,2,-1,-4]
print(*three_Sum(nums),sep='\n')
