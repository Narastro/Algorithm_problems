# 2021.10.18. 2021 Baekjoon algorithm problem #1913
# 달팽이

'''
역시 이런 문제를 많이 풀어봐야 되는군
1. 타입 에러가 자꾸 떴다. 결과값을 스트링 배열로 만들지 않은게 원인이었다.
2. 찾는 값이 1일 때를 생각하지 못했다. 초기 배열을 시작 위치로 넣어줘서 해결했다.
'''

N = int(input())
target = int(input())
table = [[0]*N for _ in range(N)]
dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]

half = 2
direction = 0
go_straight = 1
x, y = N//2, N//2
table[y][x] = '1'

num = 2
target_loc = [str(y+1), str(x+1)]
while True:
    for _ in range(half):
        for _ in range(go_straight):
            x += dx[direction]
            y += dy[direction]
            table[y][x] = str(num)
            if num == target:
                target_loc[0] = str(y+1)
                target_loc[1] = str(x+1)
            num += 1
        direction = (direction + 1) % 4
    go_straight += 1
    if go_straight == N:
        break

for _ in range(go_straight-1):
    x += dx[direction]
    y += dy[direction]
    table[y][x] = str(num)
    if num == target:
        target_loc[0] = str(y+1)
        target_loc[1] = str(x+1)
    num += 1

for i in range(N):
    print(' '.join(table[i]))
print(' '.join(target_loc))
