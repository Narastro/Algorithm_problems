# 2021.03.18. Leetcode algorithm problem #349
# Intersection of Two Arrays



def intersection(nums1:list[int], nums2:list[int])->list[int]:
    result = set()

    nums1.sort()
    nums2.sort()

    i,j = 0,0

    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i +=1
        elif nums1[i] < nums2[j]:
            j += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1
    return result

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1,nums2))