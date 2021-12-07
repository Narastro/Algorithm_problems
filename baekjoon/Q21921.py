# 2021.10.08. Baekjoon algorithm problem #21921
# 블로그

'''
쉬움
'''

N, X = map(int, input().split())
blog = list(map(int, input().split()))

start, end = 0, X-1
max_val = 0

while end < N:
    sub = blog[start:end+1]
    if max_val <= sum(sub):
        max_val = max(max_val, sum(sub))
    start += 1
    end += 1
