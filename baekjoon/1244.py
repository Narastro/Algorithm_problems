# 2021.12.26. Baekjoon algorithm problem #1244
# 스위치 켜고 끄기

N = int(input())
switch = list(map(int, input().split()))
T = int(input())


def switch_toggle(number):
    switch[number-1] = 1-switch[number-1]


for _ in range(T):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(1, N//n+1):

            switch_toggle(i*n)
    else:
        switch_toggle(n)
        left, right = n-1, n+1
        while left >= 1 and right <= N:
            switch_toggle(left)
            switch_toggle(right)
            left -= 1
            right += 1
for k in range(N//20+1):
    print(*switch[k*20:(k+1)*20])
