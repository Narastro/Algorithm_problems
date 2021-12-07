# 2021.05.26. Baekjoon algorithm problem #1747
# 소수&팰린드롬

from collections import deque

def find_prime(N):
    if N==1:
        return False
    if N==2:
        return True
    for i in range(2,N):
        if N%i==0:
            return False
    
    return True


def find_pal(N):
    str_N = deque(str(N))
    while len(str_N)>1:
        if str_N.popleft() != str_N.pop():
            return False
    return True



N = int(input())


while True:
    if find_pal(N) and find_prime(N):
            print(N)
            break
    N += 1