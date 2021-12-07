# 2021.04.21. Baekjoon algorithm problem #1303
# War

# 1. DFS 함수
def dfs(i,j,team):
    # 1-1. 범위 밖을 벗어난 경우 종료
    if i<0 or i>=N or\
    j<0 or j>=M or\
    table[j][i]!=team:
        return

    # 1-2. 방문한 값은 #으로 표시
    table[j][i] = '#'
    # 1-3. 현재 팀에 따라 점수를 1 올려줌
    if team == 'B':
        BW_score[0] += 1
    elif team == 'W':
        BW_score[1] += 1
    # 1-4. 상하좌우 재귀방문
    dfs(i+1,j,team)
    dfs(i-1,j,team)
    dfs(i,j+1,team)
    dfs(i, j-1, team)

    return

# 2. 초기값 세팅
N, M = map(int, input().split())
table = [list(map(str, input())) for _ in range(M)]
BW_score = [0, 0]
B = 0
W = 0
# 3. 각 지점에 대해 DFS 함수 호출
for j in range(M):
    for i in range(N):
        # 3-1. 호출 후 BW에 저장된 값의 제곱을 한 후 초기화
        if table[j][i] == 'B':
            dfs(i,j,'B')
            B += BW_score[0]**2
            BW_score[0]=0
        elif table[j][i] == 'W':
            dfs(i,j,'W')
            W += BW_score[1]**2
            BW_score[1] = 0

print(W,B)
