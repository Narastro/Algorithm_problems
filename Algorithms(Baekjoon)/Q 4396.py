# 2021.05.06. Baekjoon algorithm problem #4396
# Minecraft

import sys
input = sys.stdin.readline

dx = [-1,0,1,1,1,0,-1,-1]
dy = [1,1,1,0,-1,-1,-1,0]

n = int(input())
table = [list(map(str,input().rstrip())) for _ in range(n)]
answer = [['.']*n for _ in range(n)]

flag = False
for i in range(n):
    line = list(map(str,input().rstrip()))
    for j in range(n):
        if line[j] == 'x':
            if table[i][j] == '*':
                flag = True
                break
            else:
                mine = 0
                for k in range(8):
                    x = j + dx[k]
                    y = i + dy[k]
                    if 0<=x<n and 0<=y<n and table[y][x] =='*':
                        mine += 1
                answer[i][j] = str(mine)
if flag:
    for v in range(n):
        print(''.join(table[v]))
else:
    for w in range(n):
        print(''.join(answer[w]))


