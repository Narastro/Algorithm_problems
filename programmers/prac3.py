def solution(ads):
    answer = 0
    time = 0

    ads.sort(key=lambda x: (x[0], -x[1]), reverse=True)

    first = ads.pop()
    time = first[0] + 5

    wait = []
    while ads or wait:
        while ads and ads[-1][0] <= time:
            wait.append(ads.pop())
        if not wait:
            time = ads.pop()[0] + 5
        else:
            wait.sort(key=lambda x: (time-x[0])*x[1], reverse=True)
            w = wait.pop()
            answer += (time-w[0])*w[1]
            time += 5

    return answer