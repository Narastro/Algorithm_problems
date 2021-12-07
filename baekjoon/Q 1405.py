# 2021.06.03. Baekjoon algorithm problem #1405
# 미친 로봇

n, E,W,S,N = map(int,input().split())
p = [E/100,W/100,S/100,N/100]
dx,dy = [1,-1,0,0],[0,0,-1,1]
ans = 0

def dfs(i,j,k,prob,visit):
    global ans
    if k == n:
        ans += prob
        return

    for q in range(4):
        x = i+dx[q]
        y = j+dy[q]
        if (x,y) not in visit:
            visit.append((x,y))
            dfs(x,y,k+1,prob*p[q],visit)
            visit.pop()

dfs(0,0,0,1,[(0,0)])
print(ans)
        



