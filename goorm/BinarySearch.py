# 2021.12.20. goorm level
# Binary Search


def binary_search(N, li, target):
    start = 0
    end = N-1
    while start < end:
        mid = (start+end)//2
        if li[mid] == target:
            return mid+1
        elif li[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 'X'


N = int(input())
num_list = list(map(int, input().split()))
target = int(input())

print(binary_search(N, num_list, target))
