# 2021.11.20. Baekjoon algorithm problem #2224
# 최단 거리

import sys
input = sys.stdin.readline

RANGE = 58
OFFSET = 65
N = int(input())
prop_arr = [[0]*RANGE for _ in range(RANGE)]
cnt = 0
for _ in range(N):
    prop = input()
    if prop[0] == prop[5]:
        continue
    if not prop_arr[ord(prop[0])-OFFSET][ord(prop[5])-OFFSET]:
        prop_arr[ord(prop[0])-OFFSET][ord(prop[5])-OFFSET] = 1
        cnt += 1

for k in range(RANGE):
    for i in range(RANGE):
        for j in range(RANGE):
            if i != j and not prop_arr[i][j] and prop_arr[i][k] and prop_arr[k][j]:
                prop_arr[i][j] = 1
                cnt += 1

print(cnt)
for i in range(RANGE):
    for j in range(RANGE):
        if prop_arr[i][j]:
            print(chr(i+OFFSET) + " => " + chr(j+OFFSET))
