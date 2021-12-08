# 2021.04.30. Baekjoon algorithm problem #11728
# Merge Array

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A_list = list(map(int,input().split()))
B_list = list(map(int, input().split()))
answer = []
i,j = 0,0

while i<len(A_list) and j<len(B_list):
    if A_list[i] < B_list[j]:
        answer.append(A_list[i])
        i += 1
    elif A_list[i] > B_list[j]:
        answer.append(B_list[j])
        j += 1
    else:
        answer.append(A_list[i])
        answer.append(B_list[j])
        i += 1
        j += 1

if i != len(A_list):
    answer += A_list[i:]
elif j != len(B_list):
    answer += B_list[j:]

print(*answer)
