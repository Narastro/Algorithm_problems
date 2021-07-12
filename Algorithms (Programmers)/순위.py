# 2021.07.12. 2021 Graph(Programmers High score kit) 
# 순위

'''
<풀이 아이디어>
1) 선수의 수(100명)와 경기 결과(4500개)가 매우 적다?
    - 완전탐색..? 선수별로 여러 번 돌려도 되겠는데?
2) 순위를 어떻게 결정짓는거지?
    - 내가 이긴 애한테 진 애들은 다 내가 이긴게 된다?!
    - 비효율적이더라도 모든 경우를 다 달아주자.
    - 중복을 없애기 위해 set을 쓰자.
'''

from collections import defaultdict
def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)    # 이긴 애들
    lose_graph = defaultdict(set)   # 진 애들
    for winner,loser in results:        # 결과에서 이기고 진 애들 그래프화
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1,n+1):         
        for winner in win_graph[i]:                    # i한테 진 애들은 i를 이긴 애들한테도 진 것
            lose_graph[winner].update(lose_graph[i])
        for loser in lose_graph[i]:                     # i한테 이긴 애들은 i한테 진 애들한테도 이긴 것
            win_graph[loser].update(win_graph[i])
    
    for i in range(1,n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:   # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer

print(solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))