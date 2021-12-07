# 2021.10.17. 2021 Baekjoon algorithm problem #20207
# 달력

from collections import defaultdict
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
answer = 0

calendar = defaultdict(int)
for start, end in schedule:
    for i in range(start, end+1):
        calendar[i] += 1

days = sorted(calendar.keys())
pre_day = days[0]
max_cnt = 0
cnt = 0
for day in days:
    if day == days[0]:
        max_cnt = calendar[day]
        cnt += 1
        pre_day = day
        continue

    if day-pre_day == 1:
        max_cnt = max(max_cnt, calendar[day])
        cnt += 1
    else:
        answer += max_cnt * cnt
        max_cnt = 0
        cnt = 1

    pre_day = day

if max_cnt > 0:
    answer += max_cnt * cnt
else:
    answer += calendar[days.pop()]

print(answer)
