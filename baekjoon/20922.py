# 2021.04.30. Baekjoon algorithm problem #20922
# Hate Overlap
import sys,collections
input = sys.stdin.readline
N,K = map(int,input().split())
sequence = list(map(int,input().split()))
counts = collections.defaultdict(int)

start, end = 0,0
max_length = 0
while end<N:
    if counts[sequence[end]] < K:
        max_length = max(max_length, end-start+1)
        counts[sequence[end]] += 1
        end += 1
    else:
        counts[sequence[start]] -= 1
        start += 1        

print(max_length)

