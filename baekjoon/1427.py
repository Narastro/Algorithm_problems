# 2021.02.10. Baekjoon algorithm problem #1427
# Sort inside

import sys

N=sys.stdin.readline().rstrip()
print(*sorted(N,reverse=True),sep='')