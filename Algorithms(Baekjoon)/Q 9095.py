# 2021.06.15. Baekjoon algorithm problem #9095
# 1,2,3 더하기

'''
<다른 풀이> 그리디
t = int(input())
ott = [1, 2, 4]
for i in range(3, 10):
    ott.append(ott[i - 3] + ott[i - 2] + ott[i - 1])
for i in range(t):
    n = int(input())
    print(ott[n - 1])
'''

from itertools import product

nums_list = [1,2,3]

def find_method(N):
    cnt = 0
    for k in range(1,N+1):
        tmps = product(nums_list,repeat=k)
        for tmp in tmps:
            if sum(tmp) == N:
                cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    N = int(input())
    print(find_method(N))