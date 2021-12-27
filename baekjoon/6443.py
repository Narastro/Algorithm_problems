# 2021.12.27. Baekjoon algorithm problem #6443
# 애너그램

import itertools
import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    s = list(input().rstrip())
    anagram = set(itertools.permutations(s, len(s)))
    for word in sorted(list(anagram)):
        print(''.join(word))
