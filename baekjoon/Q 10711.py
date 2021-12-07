# 2021.06.11. Baekjoon algorithm problem #10711
# 모래성

'''
    처음 풀이는 단순 구현 형식으로 풀었으나 시간초과에 걸렸다.
    최종 풀이는 숫자를 기준으로 8방향이 아닌,
    모래를 기준으로 8방향의 숫자를 1씩 빼주면서
    0이 되는 지점을 새로운 모래로 지정하였고
    다시 새로운 모래를 기준으로 1씩 빼면서 0이 되는 지점이 collapse에 없게되면
    리턴하는 형식으로 구현하여 풀이에 성공하였다.
'''

import sys
from collections import deque
input=sys.stdin.readline

def collapseCastle(H,W,sandCastle):
    collapse = deque()
    wave = 0
    dx,dy = [1,1,1,0,-1,-1,-1,0],[-1,0,1,1,1,0,-1,-1]

    for i in range(W):
        for j in range(H):
            if sandCastle[j][i]=='.':
                collapse.append((i,j))

    while collapse:
        c_l = len(collapse)
        
        while c_l!=0:
            c_l -= 1

            v,w = collapse.popleft()
            for k in range(8):
                x = v+dx[k]
                y = w+dy[k]
                if 0<=x<W and 0<=y<H and sandCastle[y][x]!='.':
                    sandCastle[y][x] = int(sandCastle[y][x]) - 1
                    if sandCastle[y][x] == 0:
                        collapse.append((x,y))
        wave += 1
    return wave-1

H,W = map(int,input().split())
sandCastle = [list(input().rstrip()) for _ in range(H)]
print(collapseCastle(H,W,sandCastle))