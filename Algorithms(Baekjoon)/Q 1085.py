# 2021.02.06. Baekjoon algorithm problem #1085
# Escape from Rectangle

x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y))
