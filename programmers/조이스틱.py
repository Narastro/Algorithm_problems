# 2021.09.27. 2021 Greedy(Programmers High score kit)
# 조이스틱

'''
<풀이 참고>
https://this-programmer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1
'''


def solution(name):
    make_name = [min(ord(alp) - ord('A'), ord('Z') - ord(alp)+1)
                 for alp in name]
    idx, answer = 0, 0
    while True:
        answer += make_name[idx]
        make_name[idx] = 0
        if sum(make_name) == 0:
            break
        left, right = 1, 1
        while make_name[idx - left] == 0:
            left += 1
        while make_name[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer
