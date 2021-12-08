# 2021.11.09. Baekjoon algorithm problem #16234
# 인구 이동

'''
<챙겨갈 것>
인구 이동 판단
- 이동한 값이 있으면 is_move에 추가해주고
- is_move가 비면 종료
pypy3로 하면 통관데, 파이썬은 시간초과가 뜨네 ㅎㅎ
'''

from collections import defaultdict

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def find_union(table, visit, i, j, N, L, R):
    union = []
    Q = []
    union.append((i, j))
    Q.append((i, j))
    visit[(i, j)] = 1
    while Q:
        x, y = Q.pop()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visit[(nx, ny)] \
                    and L <= abs(table[y][x]-table[ny][nx]) <= R:
                visit[(nx, ny)] = 1
                union.append((nx, ny))
                Q.append((nx, ny))
    return union, visit


def move_population(table, is_move, union):
    pop_sum = 0
    n = len(union)
    for x, y in union:
        pop_sum += table[y][x]
    for x, y in union:
        if table[y][x] != pop_sum//n:
            is_move[(x, y)] = 1
        table[y][x] = pop_sum//n
    return table, is_move


N, L, R = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
answer = 0

while True:
    unions = []
    visit = defaultdict(int)
    is_move = defaultdict(int)
    for i in range(N):
        for j in range(N):
            if not visit[(i, j)]:
                union, visit = find_union(table, visit, i, j, N, L, R)
                unions.append(union)
    for union in unions:
        table, is_move = move_population(table, is_move, union)

    if len(is_move) == 0:
        break

    answer += 1
print(answer)
