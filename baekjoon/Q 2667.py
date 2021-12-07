# 2021.03.08. Baekjoon algorithm problem #2667
# Numbering the complex

import sys
read = lambda : sys.stdin.readline().strip()

N = int(read())
map_block = [list(map(int,read())) for _ in range(N)]


def search_map(map:list[list[int]]):
    a=[]
    count=[]
    num=0
    def DFS(i,j):
        # terminate if not land
        if i<0 or i>=N or j<0 or j>=N or\
            map[i][j] != 1:
            return

        # visiting point return to 0
        map[i][j] = 0
        count.append(1)

        # east, west, south, north
        DFS(i + 1,j)
        DFS(i - 1, j)
        DFS(i, j + 1)
        DFS(i, j - 1)

    num_home = []
    for i in range(N):
        for j in range(N):
            if map[i][j] == 1:
                count = []
                DFS(i,j)
                num +=1
                a.append(len(count))
                # number of complex
    return num, *sorted(a)

print(*search_map(map_block),sep='\n')

