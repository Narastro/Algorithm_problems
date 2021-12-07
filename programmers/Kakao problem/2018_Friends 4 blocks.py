# 2021.04.01. 2018 KAKAO Blind Recruitment
# Friends 4 Blocks

def solution(m, n, board):
    board = [list(x) for x in board]
    same_block =True

    while same_block:
        # 1. Match Determination
        same_block =[]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i][j+1] ==\
                    board[i+1][j] ==board[i+1][j+1] !='팡!':
                    same_block.append([i,j])
        # 2. Delete Matching Locations
        for i,j in same_block:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '팡!'
        # 3. Free Space Processing
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j] == '팡!':
                        board[i+1][j], board[i][j] = board[i][j] , '팡!'
    # 4. Counting the '팡!'
    return sum(x.count('팡!') for x in board)



print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))