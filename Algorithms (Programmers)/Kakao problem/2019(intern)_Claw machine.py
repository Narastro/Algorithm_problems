# 2021.03.29. 2019 KAKAO winter internship
# Claw machine

def solution(board, moves):
    # 1. initialization
    basket = []
    answer = 0
    N = len(board)
    # 2. using stacks(basket)
    for move in moves:
        # 2-1. Search from top to bottom
        for i in range(N):
            if board[i][move-1] != 0:
                pick = board[i][move-1]
                # 2-2. remove from stacks if same
                if basket and basket[-1] == pick:
                    answer += 2
                    basket.pop()
                # 2-3. else, stack
                else:
                    basket.append(pick)
                # 2-4. change to 0 and break
                board[i][move-1] = 0
                break
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]	))
