# 2021.03.02. Leetcode algorithm problem #17
# Letter Combinations of a Phone Number


digits = input()
def dfs(index, path):
    # backtracking if it is the end
    if len(path) == len(digits):
        result.append(path)
        return

    # for loop
    for i in range(index, len(digits)):
        # repeat all strings corresponding to a number
        for j in dic[digits[i]]:
            dfs(i+1,path+j)

dic = {'2':'abc','3':'def','4':'ghi','5':'jkl',
       '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
result=[]
if not digits:
    print('No')
else:
    dfs(0,'')
    print(result)