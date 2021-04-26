# 2021.04.26. Baekjoon algorithm problem #8972
# ROBOTI
import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,0,1,-1,0,1,-1,0,1]
dy = [1,1,1,0,0,0,-1,-1,-1]

def move_robots():
    Q_len = len(Q_robots)
    ix,iy = my_pos[-1]
    while Q_len :
        Q_len -= 1
        x,y = Q_robots.popleft()
        board[y][x] = '.'
        min_x, min_y = 200,200
        for k in range(9):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and ny >= 0:
                if abs(ix-nx)+abs(iy-ny) < abs(ix-min_x)+abs(iy-min_y):
                    min_x = nx
                    min_y = ny
        if board[min_y][min_x] == 'R':
            board[min_y][min_x] = '*'
            Q_robots.remove((min_x,min_y))
        elif board[min_y][min_x] == 'I':
            return -1
        elif board[min_y][min_x] == '*':
            continue
        else:
            board[min_y][min_x] = 'R'
            Q_robots.append((min_x,min_y))


def move_me(num):
    x,y = my_pos.pop()
    board[y][x] = '.'
    nx = x+dx[num-1]
    ny = y+dy[num-1]
    
    if board[ny][nx] == 'R':
        return -1

    board[ny][nx] = 'I'
    my_pos.append((nx,ny))
    if move_robots() == -1:
        return -1
    
    

R,C = map(int,input().split())
board = [list(map(str,input().rstrip())) for _ in range(R)]
moves = list(map(int,input().rstrip()))
Q_robots = deque()
my_pos = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'I':
            my_pos.append((j,i))
        elif board[i][j] == 'R':
            Q_robots.append((j,i))
time = 0
for move in moves:
    time += 1
    if move_me(move) == -1:
        print(f"kraj {time}")
        break
else:
    for w in range(R):
        for h in range(C):
            if board[w][h] == '*':
                print('.',end='')
            else:
                print(board[w][h], end='')
        print('')