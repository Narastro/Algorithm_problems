# 2021.02.09. Baekjoon algorithm problem #1436
# Shom, the movie director

N=int(input())
sentence = 666      # first

# find sentence '666'
while N != 0:
    if '666' in str(sentence):
        N = N-1
        if N == 0:
            break
    sentence = sentence + 1     # increasing by 1
print(sentence)