# 2021.02.26. Baekjoon algorithm problem #2164
# Card 2

import collections

N = int(input())
cards = collections.deque()

# making cards
for i in range(1,N+1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(*cards)

