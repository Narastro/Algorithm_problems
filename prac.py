from collections import deque

def solution(rows, columns, queries):
    answer = []
    matrix = []
    for k in range(rows):
        matrix.append([k*columns + n for n in range(1,columns+1)])
    print(matrix)
    for query in queries:
        a = deque()
        for j in range(query[1], query[3] + 1):
            a.append(matrix[query[0]-1][j-1])
        for i in range(query[0]+1,query[2]+1):
            a.append(matrix[i-1][query[3]-1])
        for j in range(query[3]-1,query[1]-1,-1):
            a.append(matrix[query[2]-1][j-1])
        for i in range(query[2]-1,query[0]-1+1,-1):
            a.append(matrix[i-1][query[1]-1])

        answer.append(min(a))
        a.appendleft(a.pop())


        for j in range(query[1], query[3] + 1):
            matrix[query[0]-1][j-1] = a.popleft()
        for i in range(query[0]+1,query[2]+1):
            matrix[i - 1][query[3] - 1] = a.popleft()
        for j in range(query[3]-1,query[1]-1,-1):
            matrix[query[2] - 1][j - 1] = a.popleft()
        for i in range(query[2]-1,query[0]-1+1,-1):
            matrix[i - 1][query[1] - 1] = a.popleft()

        print(matrix)

    return answer

print(solution(100,97,[[1,1,100,97]]))