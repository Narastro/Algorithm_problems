# 2021.02.08. Baekjoon algorithm problem #1002
# Turret

T=int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    d=((x1-x2)**2+(y1-y2)**2)**0.5                  # distance
    if x1==x2 and y1==y2:                           # if same point
        print([0,-1][r1==r2])
    elif r1+r2<d or abs(r1-r2)>d:                   # if two points do not meet
        print(0)
    else:                                           # if they meet
        print([2,1][d==r1+r2 or d==abs(r1-r2)])