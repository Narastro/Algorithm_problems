# 2021.06.03. Baekjoon algorithm problem #1525
# 퍼즐

import sys
from collections import defaultdict,deque
input = sys.stdin.readline

def bfs(sen):
    dx,dy = [1,-1,0,0],[0,0,1,-1]
    Q = deque()
    Q.append(sen)
    visit = defaultdict(int)
    visit[sen]=1
    time = -1
    while Q:
        Q_l = len(Q)
        time += 1
        while Q_l!=0:
            Q_l-=1
            s = Q.popleft()
            if s=='123456780':
                return time
            j,i = map(int,divmod(s.find('0'),3))
            for k in range(4):
                p = [list(s[0:3]),list(s[3:6]),list(s[6:9])]
                x = i+dx[k]
                y = j+dy[k]
                if 0<=x<3 and 0<=y<3:
                    tmp = '0'
                    p[j][i] = p[y][x]
                    p[y][x] = tmp
                    new_s = ''
                    for l in range(3):
                        new_s += ''.join(p[l])
                    if new_s not in visit:
                        visit[new_s] =1
                        Q.append(new_s)
    return -1




puzzle = [list(map(str,input().split())) for _ in range(3)]
pp = ''
for ii in range(3):
    pp += ''.join(puzzle[ii])
print(bfs(pp))