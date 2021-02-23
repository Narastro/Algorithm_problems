# 2021.02.23. Leetcode algorithm problem #316
# Remove Duplicate Letters

import collections

def remove_Dupli1(self, s:str)->str:
    # sort by set
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        # if full set matches suffix set
        if set(s) == set(suffix):
            return char + self.remove_Dupli1(suffix.replace(char,''))
    return ''

def remove_Dupli2(self, s:str) -> str:
    counter, seen, stack = collections.Counter(s),set(),[]

    for char in s:
        counter[char] -=1
        if char in seen:
            continue
        # remove from stack if any text left in behind
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join((stack))