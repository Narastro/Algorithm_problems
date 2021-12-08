# 2021.02.12. Baekjoon algorithm problem #9663
# N-Queen

# A function that determines if there is a queen on line
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


# Using Recursive DFS
def dfs(x):
    global result

    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
