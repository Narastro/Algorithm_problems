# 2021.02.09. Baekjoon algorithm problem #2750
# To sort numbers

N=int(input())
num=[]
for i in range(N):
    num.append(int(input()))
for i in range(N):
    print(num.pop(num.index(min(num))))
