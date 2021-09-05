# 2021.09.05. 2020 KAKAO KAKAO Blind Recruitment
# 자물쇠와 열쇠

def solution(key, lock):
    n = len(key)
    N = len(lock)
    # 1. key가 들어갈 수 있는만큼 확장
    # 2. lock 배치

    def expansion(n):
        N += n
        new_map = []
        return N

    # 3. key 시계방향 회전
    # 4. key 배치(2)
    # 5. lock 초기화
    def lotate(n):
        new_key = []
        for i in range(n):
            print(key[:][i])
        return new_key
    print(lotate(1))

    


    # key가 들어맞는지 판단
    def check():
        for j in range(len(lock)):
            for i in range(len(lock)):
                1

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))