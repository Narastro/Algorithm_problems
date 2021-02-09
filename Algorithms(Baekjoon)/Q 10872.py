# 2021.02.08. Baekjoon algorithm problem #10870
# Fibonacci's number

n=int(input())
s=[0,1]
for i in range(n):
    s.append(s[i]+s[i+1])
print(s[n])