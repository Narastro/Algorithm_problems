# 2021.05.17. Baekjoon algorithm problem #3190
# 뱀

import sys
from collections import deque
input = sys.stdin.readline


def solution(N, board, dir_info):

    dx,dy = [1,0,-1,0],[0,1,0,-1]
    x,y = 0,0
    snake = deque()
    snake.append((x,y))
    board[0][0] = 1
    direct = 0
    time = 0

    for d in dir_info:
        X,C = int(d.split()[0]), str(d.split()[1])
        for _ in range(X-time):
            time += 1
            x += dx[direct%4]
            y += dy[direct%4]
            # inside
            if 0>x or x>=N or 0>y or y>=N:
                return time

            else:
                # Apple
                if board[y][x] == -1:
                    board[y][x] = 1
                    snake.append((x,y))
                # Blank
                elif board[y][x] == 0 :
                    board[y][x] = 1
                    snake.append((x,y))
                    i,j = snake.popleft()
                    board[j][i] = 0
                # Snake body
                else:
                    return time
            
        if C == 'D':
            direct += 1
        else:
            direct -= 1

    # Straight without change of direction
    while 0<=x<N and 0<=y<N:
        x += dx[direct % 4]
        y += dy[direct % 4]
        time += 1
        if board[y][x] == -1:
            board[y][x] = 1
            snake.append((x, y))
        elif board[y][x] == 0 :
            board[y][x] = 1
            snake.append((x,y))
            i,j = snake.popleft()
            board[j][i] = 0
        else:
            return time
    
    return time

N = int(input())
board = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    y,x = map(int,input().split())
    board[y-1][x-1] = -1

L = int(input())
dir_info = []
for _ in range(L):
    dir_info.append(input().rstrip())

print(solution(N,board,dir_info))
