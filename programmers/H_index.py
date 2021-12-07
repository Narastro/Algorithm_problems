# 2021.04.19. 2021 Programmers High score kit
# H-index

def solution(citations):
    citations.sort(reverse=True)
    for i,cit in enumerate(citations):
        if i+1 >= cit:
            return cit
    return citations[0]