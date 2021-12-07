# 2021.05.03. 2021 Programmers High score kit
# Training clothes

def solution(n, lost, reserve):
    finding = 0
    n_lost = len(lost)
    for j in reserve:
        if j in lost:
            lost.remove(j)
            reserve.remove(j)
            finding += 1

    for p in lost:
        for h in reserve:
            if abs(p-h) <= 1:
                finding += 1
                reserve.remove(h)
                break
    return n - (n_lost - finding)
    

print(solution(5, [2, 4], [1, 3, 5]))
