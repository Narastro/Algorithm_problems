# 2021.03.02. Leetcode algorithm problem #3
# Longest Substring Without Repeating Characters

def length_of_Longest_Substring(s:str)->int:
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # if texts have already apeared
        if char in used and start <= used[char]:
            start = used[char] + 1
        else:
            max_length = max(max_length, index - start +1 )
        # the location of current character
        used[char] = index

    return max_length
