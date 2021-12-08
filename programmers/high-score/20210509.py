# My Answer

# def solution(code, day, data):
#     answer = []
#     stack = []
#     for d in data:
#         price = d.split()[0].split('=')[1]
#         d_code = d.split()[1].split('=')[1]
#         time = d.split()[2].split('=')[1]
#         if d_code == code and time[:8]==day:
#             stack.append((time,price))

#     stack.sort(key=lambda x:x[0]) 

#     for k in stack:
#         answer.append(int(k[1]))

#     return answer


# print(solution("012345", "20190620", ["price=80 code=987654 time=2019062113", "price=90 code=012345 time=2019062014",
#       "price=120 code=987654 time=2019062010", "price=110 code=012345 time=2019062009", "price=95 code=012345 time=2019062111"]))












# from collections import deque
# def solution(t, r):
#     answer = []
#     tr = []
#     time = 0
#     # 0:시간 1: 인덱스 2:우선순위
#     for i,v in enumerate(t):
#         tr.append((v,i,r[i]))

#     tr.sort(key=lambda x:(x[2],x[1]), reverse=True)
#     time = 0
#     index = -1
#     wait = deque()
#     while tr or wait:
#         if wait:
#             if tr[index][0] <= time:
#                 while tr[index][0] <= time:
#                     wait.append(tr.pop()[1])
#                     index -= 1
#                 wait.sort(key=lambda x: (x[2],x[1]), reverse=True)
#                 answer.append(wait.pop()[1])
#             else:
#                 wait.sort(key=lambda x: (x[2], x[1]), reverse=True)
#                 answer.append(wait.pop()[1])
#             answer.append(wait.pop()[1])
#         elif tr[index][0] <= time:
#             answer.append(tr.pop()[1])
#         else:
#             wait.appendleft(tr[index])
        
#         index -= 1
#         time += 1

#     return answer


# print(solution([0, 1, 3, 0], [0, 1, 2, 3]))


from collections import deque

def bfs(i,j,p):
    discovered= []
    ans = 0
    Q = deque()
    Q.append((i,j))
    while Q:
        v,w = Q.popleft()
        for k in range(4):
            x = v+dx[k]
            y = w+dy[k]
            if (x,y) not in discovered and x:
                discovered.append((x,y))
                Q.append((x,y))
                if maps[y][x] <= p:
                    ans += 1

    return ans



def solution(maps, p, r):
    answer = 0
    return answer


print(solution([[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [
      58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29], [39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]],19,6))
