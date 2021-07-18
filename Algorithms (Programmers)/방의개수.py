# 2021.07.18. 2021 Graph(Programmers High score kit) 
# 방의 개수

'''
<풀이 아이디어>
1) 선을 긋는 것을 어떻게 표현할까?
2) 방을 찾으려면 어떤 방법을 써야할까?
    - 기존의 점과 만날 때 방이 하나씩 생긴다?
3) 대각선이 교차하는 경우는 어떻게 할까?
    - ... 풀이를 참고했다.
    - " 이동거리를 2로 하면 중간에 노드 하나가 생기게 된다...! 즉 2)를 이용할 수 있다!
4) 왔다갔다 하는 것도 처리해야한다! (문제 풀다 발견함. 테스트케이스 1개는 심했다!)
'''

from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x,y = 0,0
    dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

    for arrow in arrows:
        for _ in range(2):              # 대각선 판별을 위해 2씩
            nx = x + dx[arrow]
            ny = y + dy[arrow]  
            if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]:    # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
                answer += 1
                visit[(x,y)].append((nx,ny))
                visit[(nx,ny)].append((x,y))
            elif (nx,ny) not in visit:                  # 방문하지 않았던 경우
                visit[(x,y)].append((nx,ny))            # 경로가 겹치는 경우는 따로 해줄 필요 없음
                visit[(nx,ny)].append((x,y))
            x,y = nx, ny        # 이동
    return answer