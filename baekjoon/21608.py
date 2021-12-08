# 2021.10.13. 2021 Baekjoon algorithm problem #21608
# 아기 상어


'''

'''

from collections import defaultdict
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]


def find_condition(N, table, like_list):

    like_cnt = defaultdict(list)
    blank_cnt = defaultdict(int)
    for j in range(N):
        for i in range(N):
            if table[j][i] == 0:
                like = 0
                blank = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        if table[ny][nx] in like_list:
                            like += 1
                        if table[ny][nx] == 0:
                            blank += 1
                like_cnt[like].append((i, j))
                blank_cnt[(i, j)] = blank

    max_like = max(like_cnt.keys())
    if len(like_cnt[max_like]) == 1:
        return like_cnt[max_like].pop()

    cond2 = defaultdict(list)
    for x, y in like_cnt[max_like]:
        cond2[blank_cnt[(x, y)]].append((x, y))

    max_blank = max(cond2.keys())
    if len(cond2[max_blank]) == 1:
        return cond2[max_blank].pop()

    cond2[max_blank].sort(key=lambda x: (x[1], x[0]))
    return cond2[max_blank].pop(0)


def satisfy_cnt(N, table, like_list):
    answer = 0
    for j in range(N):
        for i in range(N):
            cnt = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N and table[ny][nx] in like_list[table[j][i]]:
                    cnt += 1
            if cnt != 0:
                answer += 10**(cnt-1)
    return answer


N = int(input())
table = [[0]*N for _ in range(N)]
like_list = defaultdict(list)
for _ in range(N**2):
    line = input().split()
    student = line.pop(0)
    like_list[student] = line
    x, y = find_condition(N, table, line)
    table[y][x] = student
print(satisfy_cnt(N, table, like_list))
