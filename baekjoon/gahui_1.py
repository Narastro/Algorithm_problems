# 제 1회 가희 코딩테스트
# 1번

import sys
input = sys.stdin.readline

R,C = map(int,input().split())
Rg,Cg,Rp,Cp = map(int,input().split())

table = [list(map(str,input)) for _ in range(R+2)]
