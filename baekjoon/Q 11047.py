# 2021.03.16. Baekjoon algorithm problem #11047
# Coins 0

import sys
read = lambda : sys.stdin.readline()

N,K = map(int,read().split())
coin_val = []

# list of coin-value
for _ in range(N):
    coin_val.append(int(read()))

count = 0
while K!=0:
    val = coin_val.pop()
    if val > K:
        continue
    # counting
    count += K//val
    # modifying K
    K -= (K//val)*val

print(count)