# 2021.03.18. Leetcode algorithm problem #122
# Best Time to Buy and Sell Stock 2

def maxProfit(prices : list[int])->int:
    return sum(max(prices[i+1]-prices[i],0) for i in range(len(prices)-1))