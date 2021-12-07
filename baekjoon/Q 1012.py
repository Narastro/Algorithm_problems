# 2021.03.09. Baekjoon algorithm problem #1012
# Organic cabbage

import sys
# adjust recursive limit
sys.setrecursionlimit(10000)
# define input as read
read = lambda : sys.stdin.readline().split()

def num_worm(field:list[list[int]])->int:
    def DFS(i,j):
        # terminate if not cabbage
        if i<0 or i>=M or j<0 or j>=N or\
            field[j][i] != 1:
            return

        # visiting point return to 0
        field[j][i] = 0

        # east, west, south, north
        DFS(i + 1, j)
        DFS(i - 1, j)
        DFS(i, j + 1)
        DFS(i, j - 1)

    count = 0
    for i in range(M):
        for j in range(N):
            if field[j][i] == 1:
                # count up every recursion
                DFS(i, j)
                count += 1
    return count

T = int(input())
for _ in range(T):
    M,N,K = map(int,read())
    field = [[0]*M for _ in range(N)]
    for _ in range(K):
        a,b = map(int,read())
        # Watch out for horizontal positioning
        field[b][a] = 1

    print(num_worm(field))


