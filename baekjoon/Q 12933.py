# 2021.05.06. Baekjoon algorithm problem #12933
# DUCK

import sys
input = sys.stdin.readline

S = input().rstrip()

q_stack = 0
sequence = [0,0,0]
max_duck = 0

# 길이가 5의 배수가 아닌 경우 종료
if len(S)%5 != 0:
    print(-1)
    exit()

# 각 문자를 스택에 쌓음
for letter in S:
    if letter == 'q':
        q_stack += 1
    elif letter == 'u' and sequence[0]+1 <= q_stack:
        sequence[0] += 1
    elif letter == 'a' and sequence[1]+1 <= sequence[0]:
        sequence[1] += 1
    elif letter == 'c' and sequence[2]+1 <= sequence[1]:
        sequence[2] += 1
    elif letter == 'k' and q_stack > 0 and sequence[0]>0 and \
            sequence[1] > 0 and sequence[2] >0:
        max_duck = max(max_duck,q_stack)
        q_stack -= 1
        sequence[0] -= 1
        sequence[1] -= 1
        sequence[2] -= 1

    else:
        print(-1)
        break
# 스택에 남아있는 값이 있으면 -1
else:
    if q_stack != 0 or sequence[0] != 0 or sequence[1] != 0 or\
    sequence[2] != 0:
        print(-1)
    else:
        print(max_duck)

    
