# 2021.02.23. Leetcode algorithm problem #739
# Daily Temperatures

def dailyTepmeratures(T:list[int])->list[int]:
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        # determine if the current temperature is higher than stack value
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)
    return answer