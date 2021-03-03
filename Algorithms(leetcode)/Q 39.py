# 2021.03.03. Leetcode algorithm problem #39
# Combinations Sum

def Combinations_Sum(Candidates:list[int],target:int)->list[list[int]]:
    result=[]

    def DFS(csum, index,path):
        # terminating condition
        if csum<0:
            return
        if csum == 0:
            result.append(path)
            return

        # recursive
        for i in range(index,len(Candidates)):
            DFS(csum-Candidates[i],i,path + [Candidates[i]])
    DFS(target,0,[])
    return result