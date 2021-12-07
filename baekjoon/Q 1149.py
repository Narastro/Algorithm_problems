# 2021.02.16. Baekjoon algorithm problem #1149
# RGB

# input
N=int(input())
num=[]
for i in range(N):
    num.append(list(map(int,input().split())))

# store the minimum value in the following index
for i in range(1,N):
    num[i][0]=min(num[i-1][1],num[i-1][2])+num[i][0]
    num[i][1] = min(num[i - 1][0], num[i - 1][2]) + num[i][1]
    num[i][2] = min(num[i - 1][1], num[i - 1][0]) + num[i][2]

print(min(num[N-1]))