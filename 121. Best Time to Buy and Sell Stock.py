from typing import List


def maxProfit(prices: List[int]) -> int:
    greatest_difference = 0
    current_min = prices[0]
    for price in prices[1::]:
        current_min = min(price, current_min)
        difference = price - current_min
        if difference > greatest_difference:
            greatest_difference = difference
    return greatest_difference


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))