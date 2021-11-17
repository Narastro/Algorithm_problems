# 2021.11.16. Baekjoon algorithm problem #2931
# 가스관


from collections import deque, defaultdict
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
R, C = map(int, input().split())
blocks = [list(input()) for _ in range(R)]
direction = defaultdict(list)
answer = [0, 0, '']
hacked = set()


def init():
    up = (0, -1)
    down = (0, 1)
    left = (-1, 0)
    right = (1, 0)
    direction['|'].append(up)
    direction['|'].append(down)
    direction['-'].append(left)
    direction['-'].append(right)
    direction['+'].append(up)
    direction['+'].append(down)
    direction['+'].append(right)
    direction['+'].append(left)
    direction['1'].append(right)
    direction['1'].append(down)
    direction['2'].append(up)
    direction['2'].append(right)
    direction['3'].append(left)
    direction['3'].append(up)
    direction['4'].append(left)
    direction['4'].append(down)


def bfs(i, j):
    Q = deque()
    Q.append((i, j))
    visit = defaultdict(bool)
    while Q:
        x, y = Q.popleft()
        if 0 <= x < C and 0 <= y < R and (x, y) not in visit and blocks[y][x] != '.':
            visit[(x, y)] = True
            for dx, dy in direction[blocks[y][x]]:
                nx = x + dx
                ny = y + dy
                Q.append((nx, ny))
                if blocks[ny][nx] == '.':
                    answer[1] = str(nx + 1)
                    answer[0] = str(ny + 1)
                    hacked.add((x-nx, y-ny))
    return


def find_shape():
    if len(hacked) == 4:
        return '+'
    for dir in direction:
        if dir == '+':
            continue
        for pos in direction[dir]:
            if pos not in hacked:
                break
        else:
            return dir


init()
for j in range(R):
    for i in range(C):
        if blocks[j][i] == 'M' or blocks[j][i] == 'Z':
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < C and 0 <= nj < R and blocks[nj][ni] != '.':
                    bfs(ni, nj)

answer[2] = find_shape()
print(' '.join(answer))
