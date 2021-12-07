# 2021.04.28. Leetcode algorithm problem #179
# Largest Number

class solution:
    @staticmethod
    def swap(n1,n2):
        return str(n1)+str(n2) < str(n2) + str(n1)
    
    def largestNumber(self,nums):
        i = 1
        while i < len(nums):
            j = i
            while j>0 and self.swap(nums[j-1],nums[j]):
                nums[j], nums[j-1] = nums[j-1],nums[j]
                j-=1
            i += 1
        return str(int(''.join(map(str,nums))))
