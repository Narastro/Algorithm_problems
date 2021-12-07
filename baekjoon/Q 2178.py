# 2021.03.09. Baekjoon algorithm problem #2178
# Exploring the Labyrinth

import sys, collections
read = lambda : sys.stdin.readline().rstrip()

N,M = map(int,read().split())
# main matrix
matrix = [list(read()) for _ in range(N)]
# visiting point matrix
discovered = [[0]*M for _ in range(N)]
# east, west, south, north
direction = [[1,0],[-1,0],[0,-1],[0,1]]

def min_path(matrix:list[list[str]])->int:
    def BFS(x,y):
        discovered[x][y]=1
        # using Deque
        Q = collections.deque([(x,y)])
        while Q:
            i,j = Q.popleft()
            # ending point
            if i==N-1 and j==M-1:
                break
            # moving in 4-direction
            for di,dj in direction:
                if 0 <= i+di < M  and  0 <= j+dj < N and \
                    discovered[j+dj][i+di] == 0 and\
                    matrix[j+dj][i+di] == '1':
                    # marking distance in discovered
                    discovered[j+dj][i+di] = discovered[j][i]+1
                    Q.append([i+di,j+dj])
        return discovered
    # return end-point
    return BFS(0,0)[N-1][M-1]

print(min_path(matrix))
