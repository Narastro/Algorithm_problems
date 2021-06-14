# 2021.06.14. Baekjoon algorithm problem #6603
# 로또

## 조합 구하는 문제로 매우 쉬움..

import sys,itertools
input = sys.stdin.readline

while True:
    input_list = list(map(int,input().split()))
    if input_list[0] == 0:
        break
    k = input_list[0]
    answers = itertools.combinations(input_list[1:k+1],6)
    for answer in answers:
        print(*answer,sep=' ')
    print()