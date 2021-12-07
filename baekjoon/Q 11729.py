# 2021.02.08. Baekjoon algorithm problem #11729
# Tower of Hanoi


N=int(input())
def hanoi(num,start,via,arrival):
    if num==1:
        print('{} {}'.format(start,arrival))
    else:
        hanoi(num-1,start,arrival,via)
        print('{} {}'.format(start,arrival))
        hanoi(num-1,via,start,arrival)
# Total number of trials
print(2**N-1)
# Travel path
hanoi(N,1,2,3)