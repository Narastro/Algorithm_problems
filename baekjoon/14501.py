# 2021.06.18. Baekjoon algorithm problem #14501
# 퇴사

'''
DP문제,
뒤에서부터 최대 이익과 DP를 다루면서 인덱스 0까지 오는게 포인트.
'''

import sys
input = sys.stdin.readline

def find_benefit(N):
    max_benefit = 0
    for i in range(N-1,0-1,-1):
        days,benefit = schedule[i]

        if i + days > N:
            DP[i] = max_benefit 
            continue
        
        else:
            max_benefit = max(max_benefit, benefit + DP[i+days])
            DP[i] = max_benefit

    return max_benefit


N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]
DP = [0]*(N+1)
print(find_benefit(N))


