# 2021.06.23. Baekjoon algorithm problem #12100
# 2048 게임

import sys, copy
input = sys.stdin.readline

def move(board,direction):
    
    # 상
    if direction == 1:
        for i in range(N):
            index = 0
            val = 0
            for j in range(N):
                if board[j][i] == 0:
                    continue
                elif val == 0:
                    val = board[j][i]
                else:
                    if val==board[j][i]:
                        board[index][i] = val*2
                        index += 1
                        val = 0
                    else:
                        board[index][i] = val
                        index += 1
                        val = board[j][i] 
            for k in range(index,N):
                if val != 0:
                    board[k][i] = val
                    val = 0
                else:
                    board[k][i] = 0
        return board

    
    # 하
    if direction == 2:
        for i in range(N):
            index = N-1
            val = 0
            for j in range(N-1,0-1,-1):
                if board[j][i] == 0:
                    continue
                elif val == 0:
                    val = board[j][i]
                else:
                    if val==board[j][i]:
                        board[index][i] = val*2
                        index -= 1
                        val = 0
                    else:
                        board[index][i] = val
                        index -= 1
                        val = board[j][i] 
            for k in range(index,0-1,-1):
                if val != 0:
                    board[k][i] = val
                    val = 0
                else:
                    board[k][i] = 0
        return board

    # 우
    if direction == 3:
        for j in range(N):
            index = 0
            val = 0
            for i in range(N):
                if board[j][i] == 0:
                    continue
                elif val == 0:
                    val = board[j][i]
                else:
                    if val==board[j][i]:
                        board[j][index] = val*2
                        index += 1
                        val = 0
                    else:
                        board[j][index] = val
                        index += 1
                        val = board[j][i] 
            for k in range(index,N):
                if val != 0:
                    board[j][k] = val
                    val = 0
                else:
                    board[j][k] = 0
        return board

    # 좌
    if direction == 4:
        for j in range(N):
            index = N-1
            val = 0
            for i in range(N-1,0-1,-1):
                if board[j][i] == 0:
                    continue
                elif val == 0:
                    val = board[j][i]
                else:
                    if val==board[j][i]:
                        board[j][index] = val*2
                        index -= 1
                        val = 0
                    else:
                        board[j][index] = val
                        index -= 1
                        val = board[j][i] 
            for k in range(index,0-1,-1):
                if val != 0:
                    board[j][k] = val
                    val = 0
                else:
                    board[j][k] = 0
        return board

def dfs(board,d):
    global max_val
    if d==5:
        for i in range(N):
            max_val = max(max_val,max(board[i]))
        return 

    dfs(move(copy.deepcopy(board),1),d+1)
    dfs(move(copy.deepcopy(board),2),d+1)
    dfs(move(copy.deepcopy(board),3),d+1)
    dfs(move(copy.deepcopy(board),4),d+1)


max_val = 0
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
dfs(board,0)
print(max_val)