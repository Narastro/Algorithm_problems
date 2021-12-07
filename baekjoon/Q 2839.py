# 2021.02.07. Baekjoon algorithm problem #2839
# Sugar

sugar=int(input())
bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else :
    print(-1)