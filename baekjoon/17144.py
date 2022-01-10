# 2022.01.11. Baekjoon algorithm problem #17144
# 미세먼지 안녕!


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


def diffusion():
