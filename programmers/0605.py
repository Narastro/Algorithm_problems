from collections import Counter
def solution(inputString):
    n = 1
    cnt = Counter(str(n))

    for num in inputString:
        if num in str(n):
            cnt2 = Counter(num)
        while True:
            cnt = Counter(str(n))
            while cnt:
                cnt.subtract(cnt2)
                cnt += Counter()
            n+=1
            cnt = Counter(str(n))

        
print(solution('12390111'))

#####2번

def solution(endingTime, jobs):
    answer = []
    cur_time = 0
    for job in jobs:
        if job[1]> cur_time:
            cur_time = job[1]+job[3]
        else:
            cur_time += job[3]
        
        if cur_time <= job[2] and cur_time<=endingTime:
            answer.append(job[0])

    return answer

print(solution(30,[[1, 10, 20, 6], [2, 12, 20, 8], [3, 20, 30, 2], [4, 25, 40, 10]]))



#### 3번

def solution(n, data, limit):
    answer = []
    return answer