# 2021.02.18. leetcode algorithm problem #121
# Best Time to Buy and Sell stock

import sys

def max_profit(prices:list[int])->int:
    profit=0
    min_price=sys.maxsize
    # calculation between minimum and present value
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

prices = [7,1,5,3,6,4]
print(max_profit(prices))
