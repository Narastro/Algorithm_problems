# 2021.04.02. 2018 KAKAO Blind Recruitment #1
# Dart game

def solution(dartResult):
    answer = []
    s=''
    # 1. Process for each character
    for dart in dartResult:
        # 1-1. Number
        if dart.isnumeric():
            s += dart
        # 1-2. if not number, Put s in the result value and process it
        else:
            if dart == 'S':
                answer.append(int(s))
                s = ''
            elif dart =='D':
                answer.append(int(s))
                s = ''
                answer[-1] = answer[-1]**2
            elif dart == 'T':
                answer.append(int(s))
                s = ''
                answer[-1] = answer[-1]**3
            elif dart == '*':
                answer[-1] = answer[-1] * 2
                if len(answer)>1:
                    answer[-2] = answer[-2] * 2
            elif dart == '#':
                answer[-1] = answer[-1] * (-1)
    return sum(answer)



print(solution('1S2D*3T'))