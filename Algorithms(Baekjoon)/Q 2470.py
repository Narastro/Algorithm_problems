# 2021.02.18. Baekjoon algorithm problem #2470
# Two solution

import sys
N=int(input())
solutions=list(map(int,sys.stdin.readline().split()))

solutions.sort()            # sort before two pointer

left, right = 0 , len(solutions)-1
min_value=2*10**9
min_num = []

# two pointers
while not left==right:
    # find the minimum value of absolute values
    if abs(solutions[left] + solutions[right]) <= min_value:
        min_value = abs(solutions[left] + solutions[right])     # value
        min_num = [solutions[left], solutions[right]]           # number
    # find using 2 pointers
    if solutions[left] + solutions[right] < 0:
        left +=1
    elif solutions[left] + solutions[right] > 0:
        right -= 1
    else:
        break
print(*min_num)