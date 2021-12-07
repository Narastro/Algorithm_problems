# 2021.07.12. 2021 Graph(Programmers High score kit) 
# 가장 먼 노드

'''
<풀이 핵심>
1) 1번 노드에서 가장 먼 노드
    - BFS로 하나씩 내려가면서 찾아보자!
2) 그래프를 어떻게 구성할 것인가? 
    - 리스트 형태의 dict? 2차원 배열?
    - 공간 절약을 위해 dict(해시)로 ㄱㄱ
3) 노드의 갯수를 어떻게 찾을 것이냐?
    - while문을 한 번 더 써서 Q의 길이만큼 반복해주자!
'''

from collections import defaultdict, deque
def solution(n, edges):
    # 그래프 구성
    graph = defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    # 결과 : defaultdict(<class 'list'>, {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]})
    def bfs(node, n):
        Q = deque()
        Q.append(1)
        visit = [False]*(n+1)   # 0번 인덱스부터 시작하므로
        visit[1] = True
        while Q:       
            Q_len = len(Q)
            answer = Q_len      
            while Q_len != 0:       # Q의 크기만큼 반복해줌으로써 깊이마다의 노드 갯수를 알 수 있음
                Q_len -= 1
                v = Q.popleft()     # Queue
                for next_node in graph[v]:
                    if not visit[next_node]:
                        Q.append(next_node)
                        visit[next_node] = True
        return answer

    return bfs(1,n)
    

print(solution(6,	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	))

