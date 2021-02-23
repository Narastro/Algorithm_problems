# 2021.02.23. Leetcode algorithm problem #20
# Valid Parentheses

def isValid(s:str)->bool:
    stack = []
    table = {
            ')' : '(',       # table consist of parenthesis (dictionary)
            '}' : '{',
            ']' : '['
    }
    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack)==0

parenthesis='()[]{}'
print(isValid(parenthesis))
