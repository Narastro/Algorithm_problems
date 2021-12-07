# 2021.02.06. Baekjoon algorithm problem #4153
# A right-angled triangle


while True:
    x,y,z=map(int,input().split())
    if x==0 and y==0 and z==0:              # input
        break
    s=[x,y,z]                               # list of input
    # First, take out the largest value and compare it with the smallest value
    if s.pop(s.index(max(s)))**2==s.pop(s.index(min(s)))**2+s.pop()**2:
        print('right')
    else:
        print('wrong')