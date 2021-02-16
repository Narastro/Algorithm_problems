# 2021.02.16. Baekjoon algorithm problem #1904
# 01 tile

N=int(input())

# A(n)=A(n-1)+A(n-2)
num=[0,0]
num[0]=1
num[1]=2
# memory over protection
for i in range(2,N):
    num.append((num[i-1]%15746)+(num[i-2]%15746))       #
print(num[N-1]%15746)