# 2021.03.18. Leetcode algorithm problem #167
# Two Sum 2 = Input array is sorted

def two_sum (numbers:list[int], target:int)->int:
    start, end = 0,len(numbers)-1
    index = []

    while start<end :
        if numbers[start] + numbers[end] < target:
            start += 1
        elif numbers[start] + numbers[end] > target:
            end -= 1
        else:
            index.append((start+1,end+1))
            start += 1
            end -= 1
    return index

numbers = [2,7,11,15]
print(two_sum(numbers,9))