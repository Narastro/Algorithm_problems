# 2021.02.10. Baekjoon algorithm problem #1181
# Word sort

import sys

N=int(sys.stdin.readline())
word=list()

for i in range(N):
    word.append(sys.stdin.readline().rstrip())
word=set(word)
word=list(word)                         # eliminate duplication

word.sort(key=lambda x:(len(x),x))       # word is sorted by length and alphabetically

print(*word,sep='\n')