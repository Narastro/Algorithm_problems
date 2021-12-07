# 2021.03.03. Leetcode algorithm problem #77
# Combinations

def Combination(n:int, k:int)->list[list[int]]:
    results=[]

    def DFS(elements, start:int, k:int):
        if k==0:
            results.append(elements[:])
        # recursive
        for i in range(start,n+1):
            elements.append(i)
            DFS(elements,i+1,k-1)
            elements.pop()

    DFS([],1,k)
    return results