# 2021.03.03. Leetcode algorithm problem #78
# Subsets

def Subsets(nums:list[int])->list[list[int]]:
    result = [[]]

    def DFS(index,path):
        result.append(path)

        for i in range(index,len(nums)):
            DFS(i+1,path+[nums[i]])
    DFS(0,[])

    return result