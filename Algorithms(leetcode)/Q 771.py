# 2021.02.26. Leetcode algorithm problem #771
# Jewels and Stones

def numJewels_In_Stones(J:str, S:str)->int:
    return sum(s in J for s in S)