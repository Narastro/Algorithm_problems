# 2021.05.24. Baekjoon algorithm problem #2309
# 일곱 난쟁이

from itertools import combinations

dwarf = [int(input()) for _ in range(9)]

dwarf_combi = combinations(dwarf,7)

for combi in dwarf_combi:
    if sum(combi)==100:
        print(*sorted(combi),sep='\n')
        break



