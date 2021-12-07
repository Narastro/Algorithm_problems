# 2021.03.02. Leetcode algorithm problem #200
# Number of Islands

def Num_is_Islands(self, grid:list[list[str]])->int:
    def dfs(i,j):
        # terminate if it is no longer lands
        if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1' :
            return
        grid[i][j] = 0

        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i , j+1)
        dfs(i, j-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '1':
                dfs(i,j)
                # after searching, count+1
                count += 1
    return count

