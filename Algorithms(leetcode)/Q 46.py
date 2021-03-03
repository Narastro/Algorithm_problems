# 2021.03.03. Leetcode algorithm problem #46
# Permutations

def pemute(nums:list[int])->list[int]:
    results=[]
    prev_elements=[]

    def DFS(elements):
        if len(elements)==0:
            results.append(prev_elements[:])
        # recursive
        for i in elements:
            netx_elements = elements[:]
            netx_elements.remove(i)

            prev_elements.append(i)
            DFS(netx_elements)
            prev_elements.pop()

    DFS(nums)
    return results


import itertools

def permute_itertools(nums:list[int])->list[int]:
    return list(itertools.permutations(nums))