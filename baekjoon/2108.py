# 2021.02.09. Baekjoon algorithm problem #2108
# Statistics

import sys

N=int(sys.stdin.readline())         # number of trials
num=[]              # number
cnt=[0]*(8001)      # counting
for i in range(N):
    K=int(sys.stdin.readline())
    num.append(K)   # number add
    cnt[K+4000]+=1  # counting

num.sort()      #sort

print('{}'.format(round(sum(num)/N)))       # arithmetical average
print('{}'.format(num[int(N/2)]))           # middle point

if cnt.count(max(cnt))>1:                   # more than one most frequent value
    cnt.remove(max(cnt))                    # delete the first small value of frequent value
    print(cnt.index((max(cnt)))-3999)       # print the second small value of frequent value
else:
    print(cnt.index(max(cnt))-4000)         # else, print the most frequent value
print('{}'.format(max(num)-min(num)))       # the difference between the maximum and the minimum