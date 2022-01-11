# 2022.01.11. Baekjoon algorithm problem #17144
# 미세먼지 안녕!

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


def find_pos_way(i, j):
    way = 0
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0 <= x < C and 0 <= y < R and room[y][x] != -1:
            way += 1
    return way


def diffusion(dust):
    new_dust = set()
    for i, j in dust:
        value = room[j][i]
        diffus_val = value//5
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if 0 <= x < C and 0 <= y < R and room[y][x] != -1:
                room[j][i] -= diffus_val
                room[y][x] += diffus_val
                new_dust.add((x, y))
    dust = list(set(dust).union(new_dust))


def cleaning(x, y, dir):
    return


dust = []
machine = []
for j in range(R):
    for i in range(C):
        if room[j][i] > 0:
            dust.append((i, j))
        elif room[j][i] == -1:
            machine.append(j)
machine.sort()
