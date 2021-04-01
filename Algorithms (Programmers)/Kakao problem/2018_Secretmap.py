# 2021.04.01. 2018 KAKAO Blind Recruitment
# Secret map

def solution(n, arr1, arr2):
    answer = []
    # 1. Gather array to extract each value
    for a, b in zip(arr1, arr2):
        ans_str = ''
        # 2. Gather binary numbers of n digits
        for i,j in zip(format(a,'b').zfill(n),format(b,'b').zfill(n)):
            # 3. Create result string by comparison
            if i=='0' and j == '0':
                ans_str += ' '
            else:
                ans_str += '#'
        # 4. Add string to list
        answer.append(ans_str)
    return answer

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))
