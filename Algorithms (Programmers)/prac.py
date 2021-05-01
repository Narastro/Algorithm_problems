def solution(inputString):
    answer = 0
    table = {
        ')':'(',
        '}':'{',
        ']':'[',
        '>':'<'
    }
    stack = []
    max_length = 0
    for index,letter in enumerate(inputString):
        if letter in ['(','{','[,','<']:
            stack.append(letter)
            max_length += 1
        elif letter in table:
            if stack and stack.pop() != table[letter]:
                answer = -index
                break
            elif not stack:
                answer = -index
                break
    if stack:
        answer = -index
        
    elif index == len(''.join(inputString.split()))-1 and answer != -(len(''.join(inputString.split())))-1:
        answer = max_length

    return answer


print(solution('x * (y + z) ^ 2 = ?'))
