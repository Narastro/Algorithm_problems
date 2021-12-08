# 2021.02.23. Baekjoon algorithm problem #1874
# Stack Sequence

# input
N = int(input())
sequence = [int(input()) for _ in range(N)]
# initial values
stack = []
i=1
result = []

# until all sequence complete
while len(sequence)!=0:
    # impossible
    if stack and sequence[0] < stack[-1]:
        result = []
        print('NO')
        break
    # it's the same, pop it
    elif stack and sequence[0]==stack[-1]:
        sequence.pop(0)
        stack.pop()
        result.append('-')
    # otherwise, push it
    else:
        stack.append(i)
        i += 1
        result.append('+')

print(*result,sep='\n')

