# def solution(s):
#     answer = ''
#     table = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,\
#         'six':6,'seven':7,'eight':8,'nine':9}

#     word = ''
#     for letter in s:
#         if letter.isnumeric():
#             answer += letter
#         else:
#             word += letter
#             if word in table:
#                 answer += str(table[word])
#                 word = ''

#     return answer



# def solution(places):
#     answer = [1 for _ in range(5)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]


#     def dfs(i, j, n,k):
#         if n>2:
#             return
#         elif places[k][j][i] == 'X':
#             return

#         elif n>0 and places[k][j][i] == 'P':
#             answer[k] = 0
#             return

#         for w in range(4):
#             x = i+dx[w]
#             y = j+dy[w]
#             if (x, y) not in discovered and 0<=x<5 and 0<=y<5:
#                 discovered.append((x,y))
#                 dfs(x,y,n+1,k)
    
#     for p in range(5):
#         discovered = []
#         for j in range(5):
#             for i in range(5):
#                 if places[p][j][i] == 'P':
#                     discovered.append((i,j))
#                     dfs(i,j,0,p)
#     return answer


# from collections import deque
# def solution(places):
#     answer = [1 for _ in range(5)]
#     dx = [0, 0, 1, -1]
#     dy = [1, -1, 0, 0]

#     def bfs(i, j, p):
#         discovered = [(i,j)]
#         Q = deque()
#         Q.append((i,j))
#         n = 0
#         while n!=2:
#             n += 1
#             l = len(Q)
#             while l:
#                 l -= 1
#                 v,w = Q.popleft()
#                 for k in range(4):
#                     x = v+dx[k]
#                     y = w+dy[k]
#                     if 0 <= x < 5 and 0 <= y < 5 and (x, y) not in discovered:
#                         if places[p][y][x] == 'P':
#                             answer[p] = 0
#                             return
#                         elif  places[p][y][x] != 'X':
#                             discovered.append((x, y))
#                             Q.append((x,y))
#         return

#     for p in range(5):
#         for j in range(5):
#             for i in range(5):
#                 if places[p][j][i] == 'P':
#                     bfs(i, j,p)

#     return answer




############################################################


def solution(n, k, cmd):
    answer = ['O']*n
    del_n = []
    cur = k

    for c in cmd:
        if c.split()[0] == 'D':
            t = int(c.split()[1])
            while t != 0:
                cur += 1
                if cur in del_n:
                    continue
                t -= 1

        elif c.split()[0] == 'U':
            t = int(c.split()[1])
            while t != 0:
                cur -= 1
                if cur in del_n:
                    continue
                t -= 1

        elif c.split()[0] == 'C':
            del_n.append(cur)
            if cur == n:
                while cur not in del_n:
                    cur -= 1
            else:
                while cur not in del_n:
                    cur += 1

        elif c.split()[0] == 'Z':
            v = del_n.pop()

    for num in del_n:
        answer[num] = 'X'

    return ''.join(answer)

print(solution(8, 2, ["D 2", "C", "U 3", "C",
      "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))






# from collections import defaultdict
# import heapq


# def solution(n, start, end, roads, traps):
#     graph = defaultdict(list)
#     rev_graph = defaultdict(list)

#     for road in roads:
#         graph[road[0]].append((road[1], road[2]))
#         rev_graph[road[1]].append((road[0], road[2]))

#     Q = [(0, start, [False]*(n+1))]
#     visit = []
#     visit_cnt = [0]*(n+1)

#     while Q:
#         time, node,flag = heapq.heappop(Q)
#         if node == end:
#             return time

#         if node in traps:
#             flag[node] = not flag[node]

#         if node not in visit:
#             visit_cnt[node] += 1
#             if visit_cnt[node] == 2:
#                 visit.append(node)

#             if flag[node]:
#                 for v, w in graph[node]:
#                     if flag[v]:
#                         heapq.heappush(Q, (time+w, v,flag))

#                 for v, w in rev_graph[node]:
#                     if not flag[v]:
#                         heapq.heappush(Q, (time+w, v,flag))
#             else:
#                 for v, w in rev_graph[node]:
#                     if flag[v]:
#                         heapq.heappush(Q, (time+w, v,flag))
#                 for v, w in graph[node]:
#                     if not flag[v]:
#                         heapq.heappush(Q, (time+w, v,flag))

#     return


# print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))
