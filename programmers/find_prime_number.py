# 2021.04.19. 2021 Programmers High score kit
# Find prime number

from itertools import permutations

def solution(numbers):
    answer = 0
    list_num = list(numbers)
    discovered = []

    for k in range(1,len(numbers)+1):
        for c in permutations(list_num,k):
            num = int(''.join(c))

            if num == 0 or num == 1:
                continue
            elif num not in discovered and num == 2:
                answer += 1
                discovered.append(2)
                continue
            elif num not in discovered and num > 2:
                discovered.append(num)
                for i in range(2,int(num**0.5)+1):
                    if num%i==0:
                        break
                else:answer+=1
    return answer