# 2021.06.16. Baekjoon algorithm problem #11003
# 최솟값 찾기

'''
<슬라이딩 윈도우 문제>
내가 알던 슬라이딩 윈도우 방법으로 시간초과가 나왔던 문제,
1. 데크로 윈도우 설정
2. 처음부터 탐색해가며 윈도우에 넣을 때, 큰 값은 아예 넣지 않는다
'''

import sys
from collections import deque
input = sys.stdin.readline

N,L = map(int,input().split())
A = list(map(int,input().split()))

window = deque()
results = []

for i,v in enumerate(A):

    while window and window[-1] > v:
        window.pop()
    
    window.append(v)

    if i>=L and window[0] == A[i-L]:
        window.popleft()
        
    results.append(window[0])

print(*results)