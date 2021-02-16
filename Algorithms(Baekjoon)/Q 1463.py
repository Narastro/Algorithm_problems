# 2021.02.16. Baekjoon algorithm problem #1463
# Make to 1

# input
N=int(input())
cnt=0
num=[N]

# A function that a list of possible operational finished values
def Operation(x:list):
    A=[]
    for i in x:
        A.append(i-1)
        if i%3==0:
            A.append(i//3)
        if i%2==0:
            A.append(i//2)
    return A

# counting
while 1 not in num:
    tmp=num[:]
    num=Operation(tmp)
    cnt+=1

print(cnt)