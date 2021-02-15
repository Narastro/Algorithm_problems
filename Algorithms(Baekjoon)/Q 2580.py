# 2021.02.15. Baekjoon algorithm problem #2580
# Sudoku

sudoku = [list(map(int, input().split())) for _ in range(9)]
# coordinates that need to be solved
zeros = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j]==0]

def promising(i,j):
    prom=[1,2,3,4,5,6,7,8,9]
    # row check
    for k in range(9):
        if sudoku[i][k] in prom:
            prom.remove(sudoku[i][k])
        if sudoku[k][j] in prom:
            prom.remove((sudoku[k][j]))
    # 3*3 check
    i//=3
    j//=3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if sudoku[p][q] in prom:
                prom.remove(sudoku[p][q])
    # promising number return
    return prom

# recursive DFS function

finish=False

def DFS(depth):
    global finish
    # if finished
    if finish==True:
        return
    # print when all blanks are filled
    if depth==len(zeros):
        for row in sudoku:
            print(*row)
        finish=True
        return

    else:
        # receive promising number
        (i,j)=zeros[depth]
        prom=promising(i,j)
        # put it in and use recursive function
        for num in prom:
            sudoku[i][j]=num
            DFS(depth+1)
            sudoku[i][j]=0

DFS(0)






