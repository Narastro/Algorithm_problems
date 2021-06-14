# 2021.06.14. Baekjoon algorithm problem #1062
# 가르침

'''
<풀이>
입력단계에서부터 set과 difference를 이용해 a,c,i,t,n을 제외하고 받는다
K가 5보다 작은 경우 단어를 만들 수 없으므로 바로 0을 출력하고
그렇지 않은 경우 입력받는 문자들을 2진수로 변환해준다
그리고 1부터 10000~(2의 20제곱)까지의 수를 리스트에 넣고
combinations을 이용해 만들 수 있는 단어들을 세준다
'''

import sys
from itertools import combinations
input = sys.stdin.readline

bin_dict = {'b': 20, 'd': 19, 'e': 18, 'f': 17, 'g': 16, 'h': 15, 'j': 14,
            'k': 13, 'l': 12, 'm': 11, 'o': 10, 'p': 9, 'q': 8, 'r': 7,
            's': 6, 'u': 5, 'v': 4, 'w': 3, 'x': 2, 'y': 1, 'z': 0}

def convert_words(words):
    tmp = 0b0
    for letter in words:
        tmp = tmp|(1<<bin_dict[letter])
    return tmp


N,K = map(int,input().split())
words_list = [set(input().rstrip()).difference('a','c','i','t','n') for _ in range(N)]

if K<5:
    print(0)
else:
    bin_list = [convert_words(x) for x in words_list]
    max_count = 0

    power_of_2 = []
    for i in range(21):
        power_of_2.append(2 ** i)

    for comb in combinations(power_of_2, K - 5):
        current = sum(comb)
        count = 0
        for bin_number in bin_list:
            if bin_number & current == bin_number:
                count += 1

        max_count = max(max_count, count)

    print(max_count)





    
