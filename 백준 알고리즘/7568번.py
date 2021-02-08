# 2021.02.08. Baekjoon algorithm problem #7568
# Size comparison


N=int(input())
person=[]
rank=[]
# make list (height and weight as a component)
for i in range(N):
    person.append(input())
    rank.append(1)
# compare height and weight
for j in range(N):
    for k in range(N):
        if int(person[j].split()[0])<int(person[k].split()[0])\
                and int(person[j].split()[1])<int(person[k].split()[1]):
            rank[j]+=1
print(*rank)
