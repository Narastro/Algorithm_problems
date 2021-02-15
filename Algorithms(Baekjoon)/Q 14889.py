# 2021.02.15. Baekjoon algorithm problem #14889
# Start and link

# input
N=int(input())
chart=[list(map(int, input().split())) for _ in range(N)]

flag=[False]*(N+1)

def score(x:list[int])->int:
    val=0
    for i in x:
        for j in x:
            if i==j:
                continue
            val+=chart[i-1][j-1]
    return val


def Num_case(x,depth:int,N:int):
    global start

    if depth==N/2-1:
        start.append(x)
    else:
        for i in range(2,N+1):
            if not flag[i]:
                flag[i]=True
                Num_case(x+[i],depth+1,N)
                flag[i]=False
start=[]
Num_case([1],0,N)
A=set([i for i in range(1,N+1)])
min=1000
for i in range(len(start)):
    link=A-set(start[i])
    if abs(score(list(link))-score(start[i]))<min:
        min=abs(score(list(link))-score(start[i]))

print(min)




