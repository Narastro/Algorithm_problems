# 2021.03.31. 2021 KAKAO internship
# Keypad

# 2-3-1. Distance between numbers
def find_distance(num, cur):
    loc = {'1': (0, 0), '2': (1, 0), '3': (2, 0),\
           '4': (0, 1), '5': (1, 1), '6': (2, 1),\
           '7': (0, 2), '8': (1, 2), '9': (2, 2),\
           '*': (0, 3), '0': (1, 3), '#': (2, 3)}

    return abs(loc[num][0] - loc[cur][0]) + \
           abs(loc[num][1] - loc[cur][1])


def solution(numbers, hand):
    # 1. initial value, left and right stacks
    answer = ''
    l_stack = ['*']
    r_stack = ['#']
    # 2. For each number
    for number in numbers:
        # 2-1. Left buttons
        if number in [1, 4, 7]:
            l_stack.append(number)
            answer += 'L'
        # 2-2. Right buttons
        elif number in [3, 6, 9]:
            r_stack.append(number)
            answer += 'R'
        # 2-3. Center buttons
        else:
            # 2-3-1. Distance between numbers
            l_dist = find_distance(str(number), str(l_stack[-1]))
            r_dist = find_distance(str(number), str(r_stack[-1]))
            # 2-3-2. If same, it depends on right-hand or left-hand
            if l_dist == r_dist:
                if hand == 'right':
                    r_stack.append(number)
                    answer += 'R'
                else:
                    l_stack.append(number)
                    answer += 'L'
            # 2-3-3. Choose a closer distance
            elif l_dist > r_dist:
                r_stack.append(number)
                answer += 'R'
            else:
                l_stack.append(number)
                answer += 'L'
    return answer